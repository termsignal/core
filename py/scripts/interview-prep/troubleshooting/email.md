# Email

## ■ I sent an email but the recipient didn’t get it, what happened?

## ■ Someone sent me an email but I didn’t get it, what happened?

### Headers of Emails

```
Date: Wed, 11 Apr 2012 19:55:43 -0700
From: Kyle Rankin <kyle@example.net>
To: you@gmail.com
Subject: Test Subject
Test Body
From the Library of Martin Spilovsky
ptg10701870
124 Chapter 7 ■ Why Didn’t My Email Go Through? Tracing Email Problems
Here are the full contents of the email:
Delivered-To: you@gmail.com
Received: by 10.182.250.51 with SMTP id yz19csp53077obc;
 Wed, 11 Apr 2012 19:55:45 -0700 (PDT)
Received: by 10.42.179.196 with SMTP id br4mr523278icb.42.1334199345073;
 Wed, 11 Apr 2012 19:55:45 -0700 (PDT)
Return-Path: <greenfly@example.net>
Received: from mail.example.net (mail.example.net. [64.142.5.5])
 by mx.google.com with ESMTPS id s4si19571254igb.48.2012.04.11.19.55.44
 (version=TLSv1/SSLv3 cipher=OTHER);
 Wed, 11 Apr 2012 19:55:44 -0700 (PDT)
Received-SPF: pass (google.com: best guess record for domain of greenfly@example.net
Êdesignates 64.142.5.5 as permitted sender) client-ip=64.142.5.5;
Authentication-Results: mx.google.com; spf=pass (google.com: best guess record for domain
Êof greenfly@example.net designates 64.142.5.5 as permitted sender) smtp.mail=greenfly@
Êexample.net
Received: by mail.example.net (Postfix, from userid 1000)
id 7F566254A3; Wed, 11 Apr 2012 19:55:43 -0700 (PDT)
Date: Wed, 11 Apr 2012 19:55:43 -0700
From: Kyle Rankin <kyle@example.net>
To: you@gmail.com
Subject: Test Subject
Message-ID: <20120412025543.GD23360@example.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Disposition: inline
User-Agent: Mutt/1.5.20 (2009-06-14)
Test Body
```



## Problems

### Client Can’t Communicate with the Outbound Mail Server

* Check Network
* Check DNS
* Check Ports
* Send Manual Email with Telnet
  * The telnet output has Email Error Codes for more information
  * Outbound Mail Server Won’t Allow Relay- this is an old method
  * Use your user and pw to log in to the relay


### Outbound Mail Server Can’t Communicate with the Destination

* Check the mail server outbound log
  * `/var/log/mail.log or /var/log/ maillog`
  * Use queueID + CTRL + F
  * `grep 12BDBE6FEE9 /var/log/mail.log`
* Check if you can communicate to the destination server
  * `dig gmail.com MX +short`
* Check the port
  * `nmap -p 25 gmail-smtp-in.l.google.com`
  * you might need to block ping probes
    * `nmap -p 25 -PN gmail-smtp-in.l.google.com`
* Run`mailq` to see the current status of the mail queue


### Other Troubleshooting Commands

* `sudo egrep 'to=.*jan@example.net' /var/log/mail.log > /tmp/jans_incoming_emails`
* `sudo grep 62337254A2 /var/log/mail.log`
* Check to see if the service is up`sudo /etc/init.d/postfix status`
* Check processees`ps -ef | grep postfix`
