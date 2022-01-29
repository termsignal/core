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

## High Level Design

## API Design

## Data Model

### Component Design

### Content Uploader

### Control Plane

### Video Encoder

### CDN Health Checker

### Title Indexer

### Data Plane

#### Playback Workflow

#### Content Lookup Workflow

### Optimizations

### Addressing Bottlenecks
