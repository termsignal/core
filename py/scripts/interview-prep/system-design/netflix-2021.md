# Designing Netflix

## Problem Statement

Design a video streaming platform similar to Netflix. Content creators can upload their video and viewers are able to play the videos on different devices. We should also be able to store user statistics of the videos such as a number of views, videos watched, duration... etc

## Gather Requirements

### In Scope

* Content Creators should be able to upload content at a designated time.
* The viewers are able to watch the video on different platforms (TV, mobile, etc).
* User should be able to search videos based on titles.
* The system should support subtitles for videos.

### Out of Scope

* The mechanism to recommend personalized videos to different users.
* Billing and Subscription model

## Capacity Planning

* What are the number of active daily users? DAU
  * 100 Million
* What is the average size of videos being uploaded per minute?
  * 2500 MB
* What is the total combinations of resolutions and codec formats which need to be supported?
  * 10
* What is the Average Number of Video users watch a day?
  * 3

The `Playback Microservice` is responsible for playback requests and requires many servers.

How do we calculate the amount of servers we need?

`Total Servers = `

`(Number of Playback Requests per Sec * Latency) / Number of Concurrent Connections per Server`

* Latency 20ms
* Max Connections 10k
* Scale to 75% of DAU Requesting Playback

`150 Total Servers = (75M*20ms/10K)`

Number of Videos watched per second = (Num of Active Users * Number of Average Videos Watched Daily) / 86400 Sec

* `(100 Million * 3 / 86400) = VWPS 3472`

Size of the content stored on a daily basis = ( average size of video uploaded per min * Num of pairwise combination of resolutions and codecs * 24 * 60 = 36TB/day)

* `2500MB * 10 * 24 * 60 = 36,000,000MB`
* `36,000,000 / 1024 = 36,000GB`
* `36,000 / 1024 = 36TB`
* `36TB` a day of Uploaded videos

## High Level Design

We have two user types

1. Content Creators
2. Viewers

* Content Distributor Network: Stores content in the locations which are geographically closts to users.
  * Open Connect is the global cusom CDN for netflix
* Control Plane: Component that handles uploads from content creators that will eventually hit CDNs
  * CDN Health Checker Service: This will check the health of the CDN periodically based on playback experience
  * Content Uploader Service: This will consume the content from creators and distribute it to CDNS to ensure robust playback experience. Also, stores metadata of video content.
* Data Storage: Video metadata is saved in the data storage. Including subtitle information in the optimal db
* Data Plane: Component that will interact with endusers for playback. Different platforms and returns urls of CDNs with the files requested
  * Playback Service
    * The service will determine the files that are required for playback
    * Get all URLS
  * Steering Service
    * This service determines the optimal CDN urls from which requested playback can be fetched from
    * Select best URLS

Diagram
![](assets/20220129_000952_netflix-2021-diagrams.png)

Steps

1. The content creators upload the video content to the control plane.
2. The video content gets uploaded on the CDN which are placed geographically closer to end users.
3. The CDN reports the status to the control plane such as health metrics, what files they have stored, the optimal BGP routes and so forth.
4. The video metadata and the related CDN information gets persisted in the data storage.
5. A user on the client device places the request to play a particular title (TV show or movie).
6. Playback service determines the files which are required to playback a specific title.
7. The Steering service picks the optimal CDNs from which the required files can be fetched from. It generates the urls of such CDNs and provide it to back to the client device.
8. Client device requests the CDNs to serve the requested files.
9. CDN serves the requested files to the client device which gets rendered to the users.

## API Design

#### Video Upload

Path:

POST /video-contents/v1/videos

Body:

```
{
	videoTitle : Title of the video
	videoDescription : Description of the video
	tags : Tags associated with the video
	category : Category of the video, e.g. Movie, TV Show, 
	videoContent: Stream of video content to be uploaded
}
```

#### Search Video

Path:

GET /video-contents/v1/{$search-query}

Query Parameter:

`{ user-location: location of the user performing search } `

#### Stream Video

Path:

GET /video-contents/v1/videos/

Query Parameter:

```
{
	offset: Time in seconds from the beginning of the video
}
```

### Data Model

### Component Design

#### Content Uploader

This module will execute when the creators upload content. Its responsible for distributing content to CDN
![img](assets/20220129_114220.png)

#### Control Plane

#### Video Encoder

#### CDN Health Checker

#### Title Indexer

#### Data Plane

#### Playback Workflow

#### Content Lookup Workflow

### Optimizations

### Addressing Bottlenecks
