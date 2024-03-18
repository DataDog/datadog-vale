# Vale Linter Rules

This page provides a comprehensive list of the Vale linter rules used in Datadog documentation.

Last Updated: 2024-03-18

## Table of Contents
- [Vocab](#vocab)
- [CWS-Descriptions](#cws-descriptions)
- [SIEM-Names](#siem-names)
- [Datadog](#datadog)
- [CWS-Names](#cws-names)

## Vocab


## CWS-Descriptions

### Refer to the 'Datadog %s' instead of the 'Datadog %s'

**Level:** *error*

**Swap:**
- `agent` -> `Agent`

**Ignore Case:** False


## SIEM-Names

### Rule names should use sentence case

**Level:** *error*

**Exceptions:**
- `1Password`
- `Advanced Protection`
- `Autoscaling Group`
- `Amazon EC2 Instance`
- `Amazon S3`
- `API calls`
- `Auth0 Attack Protection`
- `Auth0 Breached Password Detection`
- `Auth0 Brute Force Protection`
- `Auth0 Guardian MFA`
- `Auth0 Suspicious IP Throttling`
- `AWS Cloudtrail GetCallerIdentity`
- `AWS DescribeInstances`
- `AWS IAM User created with AdministratorAccess policy attached`
- `AWS ConsoleLogin`
- `AWS Console login without MFA`
- `AWS GuardDuty`
- `AWS IAM Roles Anywhere`
- `AWS Kinesis Firehose`
- `AWS Lambda`
- `AWS Network Gateway`
- `AWS Secrets Manager`
- `AWS Systems Manager`
- `AWS Verified Access`
- `AWS VPC Flow Log`
- `Azure Active Directory`
- `Azure AD Identity Protection`
- `Azure AD Privileged Identity Management`
- `CloudTrail`
- `Cloudflare`
- `Cloudflare CASB Finding`
- `Cloudflare L7 DDOS`
- `Crowdstrike Alerts`
- `Enterprise Organization`
- `GitHub`
- `GitHub Advanced Security`
- `GitHub Dependabot`
- `GitHub Personal Access Token`
- `GitHub Secret Scanning`
- `Google App Engine`
- `Google Cloud`
- `Google Cloud IAM Role updated`
- `Google Cloud Storage`
- `Google Cloud Storage Bucket`
- `Google Compute`
- `Google Compute Engine`
- `Google Drive`
- `Google Security Command Center`
- `Google Workspace`
- `IdP configuration changed`
- `Impossible Travel Auth0`
- `IoC`
- `Jamf Protect`
- `Microsoft 365 Application Impersonation`
- `Microsoft 365 Default or Anonymous`
- `Microsoft 365 E-Discovery`
- `Microsoft 365 Exchange`
- `Microsoft 365 Full Access`
- `Microsoft 365 Inbound Connector`
- `Microsoft 365 OneDrive`
- `Microsoft 365 Security and Compliance`
- `Microsoft 365 SendAs`
- `Microsoft Defender for Cloud`
- `Microsoft Intune Enterprise MDM`
- `Microsoft Teams`
- `Okta`
- `Okta Identity Provider`
- `Palo Alto Networks Firewall`
- `RDS Snapshot`
- `Scout Suite`
- `Sqreen`
- `Tor`
- `TruffleHog`
- `Zendesk Automatic Redaction`


## Datadog

### Use '%s' instead of '%s'.

**Level:** *error*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#inclusive-language)

**Swap:**
- `black ?list` -> `disallow list|exclude list`
- `master` -> `primary`
- `slave` -> `secondary`
- `white ?list` -> `allow list|include list`

**Ignore Case:** True

### Avoid vague text in links like '%s' unless you can pair it with more descriptive text.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#links)

**Swap:**
- `\[here\]\(.*?\)` -> `here`
- `<a\s*href\s*=\s*".*?".*?>\s*here\s*</a>` -> `here`
- `\[this\]\(.*?\)` -> `this`
- `<a\s*href\s*=\s*".*?".*?>\s*this\s*</a>` -> `this`
- `\[page\]\(.*?\)` -> `page`
- `<a\s*href\s*=\s*".*?".*?>\s*page\s*</a>` -> `page`
- `\[this page\]\(.*?\)` -> `this page`
- `<a\s*href\s*=\s*".*?".*?>\s*this page\s*</a>` -> `this page`

**Ignore Case:** True

### Use '%s' instead of '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#words-and-phrases)

**Swap:**
- `a number of` -> `few|several|many`
- `acknowledgement` -> `acknowledgment`
- `App Analytics` -> `Tracing without Limits™`
- `auto(?:\s|-)complete` -> `autocomplete`
- `auto(?:\s|-)completion` -> `autocompletion`
- `Availability Zone` -> `availability zone`
- `Availability Zones` -> `availability zones`
- `back(?:\s|-)end` -> `backend`
- `back(?:\s|-)ends` -> `backends`
- `bear in mind` -> `keep in mind`
- `boolean` -> `Boolean`
- `booleans` -> `Booleans`
- `cheat sheet` -> `cheatsheet`
- `command line interface` -> `command-line interface`
- `Create a new` -> `Create a|Create an`
- `culprit` -> `cause`
- `data are` -> `data is`
- `data(?:\s|-)point` -> `datapoint`
- `data(?:\s|-)points` -> `datapoints`
- `data(?:\s|-)set` -> `dataset`
- `data(?:\s|-)sets` -> `datasets`
- `data-?center` -> `data center`
- `data-?centers` -> `data centers`
- `Datadog (?:app|application)` -> `Datadog|Datadog site`
- `Datadog product` -> `Datadog|Datadog service`
- `data-?source` -> `data source`
- `data-?sources` -> `data sources`
- `default (?:dash|screen)board` -> `out-of-the-box dashboard`
- `default (?:dash|screen)boards` -> `out-of-the-box dashboards`
- `(?:Dev/?ops|dev/?ops|Dev/Ops)` -> `DevOps|DevSecOps`
- `drill (?:down|into)` -> `examine|investigate|analyze`
- `drilling (?:down|into)` -> `examining|investigating|analyzing`
- `Distributed Tracing` -> `distributed tracing`
- `(?:easy|easily)` -> ``
- `e-?book` -> `eBook`
- `e-?books` -> `eBooks`
- `e-mail` -> `email`
- `e-mailing` -> `emailing`
- `e-mails` -> `emails`
- `end(?:\s|-)point` -> `endpoint`
- `end(?:\s|-)points` -> `endpoints`
- `event (?:stream|streem)` -> `Event Stream`
- `flame-?graph` -> `flame graph`
- `flame-?graphs` -> `flame graphs`
- `figure out` -> `determine`
- `figuring out` -> `determining`
- `file(?:\s|-)name` -> `filename`
- `file(?:\s|-)names` -> `filenames`
- `filesystem` -> `file system`
- `filesystems` -> `file systems`
- `fine\s?-?tune` -> `customize|optimize|refine`
- `for the most part` -> `generally|usually`
- `front(?:\s|-)end` -> `frontend`
- `health-?check` -> `heath check`
- `health-?checks` -> `heath checks`
- `(?:heat-?map|Heat Map)` -> `heat map`
- `(?:heat-?maps|Heat Maps)` -> `heat maps`
- `(?:host-?map|Host Map)` -> `host map`
- `(?:host-?maps|Host Maps)` -> `host maps`
- `hone in` -> `home in`
- `hones in` -> `homes in`
- `honing in` -> `homing in`
- `highly` -> ``
- `hit` -> `click|select`
- `in order to` -> `to`
- `in sync` -> `in-sync`
- `In sync` -> `In-sync`
- `indices` -> `indexes`
- `indexation` -> `indexing`
- `infrastructures` -> `infrastructure`
- `install command` -> `installation command`
- `Internet` -> `internet`
- `(?:i/?-?o|I-?O)` -> `I/O`
- `(?:i/?ops|I/OPS)` -> `IOPS`
- `just` -> ``
- `keep in mind` -> `consider`
- `left up to` -> `determined by`
- `let's assume` -> `assuming|for example, if`
- `load-?balancing` -> `load balancing`
- `machine-?learning` -> `machine learning`
- `micro(?:\s|-)service` -> `microservice`
- `micro(?:\s|-)services` -> `microservices`
- `multi-?alert` -> `multi alert`
- `multicloud` -> `multi-cloud`
- `multiline` -> `multi-line`
- `Note that` -> `**Note**:`
- `(?:obvious|obviously|Obviously)` -> ``
- `off-line` -> `offline`
- `on the fly` -> `real-time|in real time`
- `Once` -> `After`
- `open-?source` -> `open source`
- `page view` -> `pageview`
- `page views` -> `pageviews`
- `play a hand` -> `influence`
- `please` -> ``
- `pre-connect` -> `preconnect`
- `quick|quickly` -> ``
- `screen(?:\s|-)board` -> `screenboard`
- `simple|simply` -> ``
- `single pane of glass` -> `single view|single place|single page`
- `slice and dice` -> `filter and group`
- `stand for` -> `represent|mean`
- `Synthetics` -> `Synthetic Monitoring`
- `reenable` -> `re-enable`
- `run(?:\s|-)time` -> `runtime`
- `refer to|visit` -> `see|read|follow`
- `time board` -> `timeboard`
- `time(?:\s|-)series` -> `timeseries`
- `time-?frame` -> `time frame`
- `time-?frames` -> `time frames`
- `top-?list` -> `top list`
- `trade(?:\s|-)off` -> `trade-off`
- `Trace Search and Analytics` -> `Tracing without Limits™`
- `turnkey` -> `ready to use`
- `under the hood` -> ``
- `utilize` -> `use`
- `very` -> ``
- `via` -> `with|through`
- `visit` -> `see|read`
- `webserver` -> `web server`
- `web site` -> `website`
- `X-axis` -> `x-axis`
- `Y-axis` -> `y-axis`
- `(?:github|Github)` -> `GitHub`
- `(?:kubernetes|k8s|K8s|K8S)` -> `Kubernetes`
- `(?:Mapreduce|mapreduce|Map reduce|Map Reduce)` -> `MapReduce`
- `memcached` -> `Memcached`
- `(?:nginx|Nginx)` -> `NGINX`
- `(?:node.js|nodeJS|NodeJS|node.JS|Node.JS)` -> `Node.js`
- `(?:pagerduty|pager duty|Pagerduty|Pager duty)` -> `PagerDuty`
- `prometheus` -> `Prometheus`
- `(?:sql|Sql)` -> `SQL`
- `(?:statsd|statsD|Statsd)` -> `StatsD`
- `(?:unix|Unix)` -> `UNIX`

**Ignore Case:** False

### Use '%s' instead of abbreviations like '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#abbreviations)

**Swap:**
- `\b(?:eg|e\.g\.|eg\.)[\s,]` -> `for example`
- `\b(?:ie|i\.e\.|ie\.)[\s,]` -> `that is`

**Ignore Case:** True

### '%s' should use sentence-style capitalization.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#headers)

**Exceptions:**
- `ACLs`
- `ActiveMQ XML Integration`
- `Agent`
- `Agentless`
- `Agents`
- `Airflow`
- `Amazon`
- `Amazon Web Services`
- `APCu`
- `APIs`
- `APM`
- `Application Performance Monitoring`
- `APM & Continuous Profiler`
- `App Analytics`
- `App Service`
- `AppVeyor`
- `Application Security Management`
- `Application Vulnerability Management`
- `AuthN`
- `Autodiscovery`
- `AWS Step Functions`
- `AWS Systems Manager`
- `Azure`
- `Azure App Service`
- `Azure App Service Plan`
- `Azure Blob Storage`
- `Azure Event Hub`
- `Audit Trail`
- `BitBucket`
- `BuildKite`
- `Browser Monitoring`
- `CakePHP`
- `Cassandra Nodetool`
- `Cassandra Nodetool Integration`
- `CentOS`
- `Chef`
- `CircleCI`
- `CI/CD`
- `CI Visibility`
- `Clipboard`
- `Cloud Cost Management`
- `Cloud Pub Sub`
- `Cloud Security Management`
- `Cloud Security Posture Management`
- `Cloud SIEM`
- `Cloud Workload Security`
- `CloudFormation`
- `CloudSQL`
- `CloudTrail`
- `CloudWatch`
- `Cluster Agent`
- `Continuous Profiler`
- `Continuous Testing`
- `DaemonSet`
- `Data Collected`
- `Database Monitoring`
- `Datadog`
- `DatadogMetric`
- `Datadog Agent Manager`
- `Datadog for Government`
- `Datadog Forwarder`
- `Datadog Lambda Extension`
- `Datadog Operator`
- `Datadog Plugin`
- `Datadog Watchdog`
- `DatadogHook`
- `Debian`
- `Detection Rules`
- `Docker`
- `Docker Compose`
- `Docker Swarm`
- `Dockerfile`
- `DogStatsD`
- `Envoy`
- `Fargate`
- `FastCGI`
- `Firehose Nozzle`
- `FireLens`
- `Fluent Bit`
- `Fluentd`
- `FreeBSD`
- `FreeSwitch`
- `Further Reading`
- `GeoIP`
- `Git`
- `GitHub`
- `GitHub Actions`
- `GitLab`
- `GitLab Runner Integration`
- `Google`
- `Google Analytics`
- `Google Cloud`
- `Google Cloud Functions`
- `GraphQL`
- `Gunicorn`
- `HAProxy`
- `HBase RegionServer Integration`
- `HDFS DataNode Integration`
- `HDFS NameNode Integration`
- `Helm`
- `Heroku`
- `HipChat`
- `HostPort`
- `I`
- `IdP`
- `IDs`
- `iLert`
- `Incident Management`
- `Infrastructure Monitoring`
- `Ingress Controller`
- `Internet Information Services`
- `IoT`
- `IPs`
- `Java`
- `JavaScript`
- `JBoss`
- `Jenkins`
- `JFrog`
- `JFrog Artifactory`
- `Jira`
- `JMXFetch`
- `Journald`
- `Kafka`
- `Kafka Consumer Integration`
- `Kubernetes`
- `Kubernetes Engine`
- `Kubernetes Pod`
- `Kubernetes Service`
- `Lambda`
- `Lambda Layer`
- `Lambda@Edge`
- `LaunchDarkly`
- `Linux`
- `Live Analytics`
- `Live Search`
- `Live Tail`
- `Log Explorer`
- `Log Management`
- `Log Rehydration`
- `Logback`
- `macOS`
- `Marketplace`
- `MarkLogic`
- `Meraki`
- `Mesos Slave Integration`
- `Metrics Explorer`
- `Metrics without Limits`
- `Mobile Monitoring`
- `MongoDB`
- `MsTest`
- `MySQL`
- `Network Address Translation`
- `Network Device Monitoring`
- `Network Performance Monitoring`
- `New Relic`
- `NGINX Plus`
- `NixOS`
- `Node`
- `Notebook`
- `Notebook List`
- `npm`
- `NXLog`
- `Observability Pipelines`
- `OkHttp`
- `OneLogin`
- `OPcache`
- `OpenLDAP`
- `OpenMetrics`
- `OpenShift`
- `OpenStack`
- `openSUSE`
- `OpenTelemetry`
- `OpenTracing`
- `OpenVPN`
- `OpsGenie`
- `OpsWorks`
- `Oracle Instant Client`
- `Phusion Passenger`
- `Pipeline Visibility`
- `Pivotal Platform`
- `Postgres`
- `PostgreSQL`
- `PowerDNS`
- `Prometheus`
- `Prometheus Alertmanager`
- `Puppet`
- `Python`
- `RabbitMQ`
- `Rails`
- `Rancher`
- `Real User Monitoring`
- `Red Hat`
- `Redis`
- `ReplicaSet`
- `RocketPants`
- `Roku Monitoring`
- `Root Cause Analysis`
- `Route53`
- `RSpec`
- `Ruby`
- `RUM`
- `RumMonitor`
- `SafeNet`
- `SaltStack`
- `Security Monitoring`
- `Security Signal`
- `Security Signals`
- `SELinux`
- `Sensitive Data Scanner`
- `Serverless APM`
- `Serverless Framework`
- `Serverless Monitoring`
- `Serverless Workload Monitoring`
- `Service Checks`
- `Session Replay`
- `Siri`
- `Slack`
- `SLIs`
- `SLOs`
- `socat`
- `Social Security`
- `SQL Server`
- `SQLDelight`
- `SQLite`
- `Stackdriver`
- `StackPulse`
- `StackStorm`
- `StatsD`
- `Sumo Logic`
- `Swift`
- `Synthetic Monitoring`
- `Syslog`
- `sysOID`
- `System Core`
- `System Swap`
- `Teamcity`
- `Terraform`
- `Testing Visibility`
- `TokuMX`
- `Tracing Without Limits`
- `Trello`
- `Twilio`
- `TypeScript`
- `Ubuntu`
- `Unified Service Tagging`
- `Unix`
- `Unix Domain Socket`
- `URLs`
- `User Datagram Protocol`
- `USM`
- `Universal Service Monitoring`
- `Varnish`
- `Vector`
- `Vertica`
- `VMWare`
- `vSphere`
- `Watchdog`
- `Watchdog Insights`
- `Webhook`
- `WildFly`
- `Windows`
- `Xray`
- `ZooKeeper`

### Missing ™ on phrase '%s'

**Level:** *error*

[Link](https://www.datadoghq.com)

**Tokens:**
- `(?<!\*)Logging without Limits(?!\s*(\™|\\\*|\*))`
- `(?<!\*)Tracing without Limits(?!\s*(\™|\\\*|\*))`
- `(?<!\*)Metrics without Limits(?!\s*(\™|\\\*|\*))`
- `(?<!\*)Log Rehydration(?!\s*(\™|\\\*|\*))`

**Ignore Case:** True

### Brett Test 3

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#dashes)

**Tokens:**
- `\s[—–]\s`

### Avoid temporal words like '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#tense)

**Tokens:**
- `currently`
- `now`
- `will`
- `won't`
- `[a-zA-Z]*'ll`

**Ignore Case:** True

### In general, use American spelling instead of '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md)

**Tokens:**
- `(?:\w+)nised`
- `(?:\w+)ise`
- `(?:\w+)logue`
- `(?:\w+)lour`
- `(?:\w+)lyse`
- `[a-zA-Z]{2,}our(?:\b|s|ed|ing)`

**Exceptions:**
- `(?:A|a)dvertise`
- `(?:A|a)dvise`
- `(?:A|a)ppraise`
- `(?:A|a)pprise`
- `(?:A|a)rise`
- `(?:C|c)hastise`
- `(?:C|c)ircumcise`
- `(?:C|c)lockwise`
- `(?:C|c)omprise`
- `(?:C|c)ompromise`
- `(?:C|c)oncise`
- `(?:C|c)ounterclockwise`
- `(?:D|d)emise`
- `(?:D|d)espise`
- `(?:D|d)evise`
- `(?:D|d)isguise`
- `(?:E|e)nterprise`
- `(?:E|e)xcise`
- `(?:E|e)xercise`
- `(?:E|e)xpertise`
- `(?:F|f)ranchise`
- `(?:I|i)mprecise`
- `(?:I|i)mprovise`
- `(?:I|i)ncise`
- `(?:L|l)ikewise`
- `(?:M|m)erchandise`
- `(?:N|n)oise`
- `(?:O|o)therwise`
- `(?:P|p)aradise`
- `(?:P|p)oise`
- `(?:P|p)raise`
- `(?:P|p)recise`
- `(?:P|p)remise`
- `(?:P|p)romise`
- `(?:R|r)evise`
- `(?:R|r)ise`
- `(?:S|s)upervise`
- `(?:S|s)urmise`
- `(?:S|s)urprise`
- `(?:T|t)elevise`
- `(?:W|w)ise`
- `(?:d|D)etours?`
- `(?:c|C)ontours?`
- `(?:g|G)lamour`
- `(?:o|O)utpour`
- `(?:s|S)cours?`
- `(?:t|T)roubadours?`
- `(?:p|P)ompadour`

**Ignore Case:** True

### Avoid first-person pronouns such as '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#pronouns)

**Tokens:**
- `(?<=^|\s)I(?=\s)`
- `(?<=^|\s)I,(?=\s)`
- `\bI'm\b`
- `(?<=\s)[Mm]e\b`
- `(?<=\s)[Mm]y\b`
- `(?<=\s)[Mm]ine\b`
- `(?<=\s)[Ww]e\b`
- `we'(?:ve|re)`
- `(?<=\s)[Uu]s\b`
- `(?<=\s)[Oo]ur\b`
- `\blet's\b`

### Avoid en dashes ('–'). For hyphenated words, use a hyphen ('-').
For parenthesis, use an em dash ('—').

**Level:** *error*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#dashes)

**Tokens:**
- `–`

### Use %s (the former, to refer to Datadog's mechanism for applying integration configurations to containers; the latter, to refer to automatic discovery IN GENERAL) instead of '%s'.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#words-and-phrases)

**Swap:**
- `{'(?:autodiscovery|auto-discovery|Auto-discovery)': 'Autodiscovery|automatic detection'}`
- `{'(?:autodiscover|auto-discover|Auto-discover)': 'Autodiscover|automatically detect'}`
- `{'(?:autodiscovered|auto-discovered|Auto-discovered)': 'Autodiscovered|automatically detected'}`

**Ignore Case:** False

### Use a gender-neutral pronoun instead of '%s'.

**Level:** *error*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#gender)

**Tokens:**
- `he/she`
- `s/he`
- `\(s\)he`
- `\bhe\b`
- `\bhim\b`
- `\bhis\b`
- `\bshe\b`
- `\bher\b`

**Ignore Case:** True

### Use only one space between words and sentences (not two).

**Level:** *error*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#spaces)

**Tokens:**
- `[\w.?!,\(\)\-":] {2,}[\w.?!,\(\)\-":]`

### Brett Test 2

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#dashes)

**Tokens:**
- `\s[—–]\s`

### Use straight quotes instead of smart quotes.

**Level:** *error*

**Tokens:**
- `“`
- `”`
- `‘`
- `’`

### Format times as 'HOUR:MINUTE a.m.' or HOUR:MINUTE p.m.' instead of '%s'.

**Level:** *warning*

[Link](https://datadoghq.atlassian.net/wiki/spaces/WRIT/pages/2732523547/Style+guide#%s)

**Tokens:**
- `(1[012]|[1-9]):[0-5][0-9] (A\.M\.|P\.M\.)`
- `(1[012]|[1-9]):[0-5][0-9] (?i)(a\.m[^\.]|p\.m[^\.])`
- `(1[012]|[1-9]):[0-5][0-9][ ]?(?i)(am|pm)`

### Use the Oxford comma in '%s'.

**Level:** *suggestion*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#commas)

**Tokens:**
- `(?:[^,]+,){1,}\s\w+\s(?:and|or)`

### Don't put a space before or after a dash.

**Level:** *warning*

[Link](https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#dashes)

**Tokens:**
- `\s[—–]\s`

### Try to keep your sentence length to 25 words or fewer.

**Level:** *suggestion*

**Ignore Case:** False


## CWS-Names

### Rule names should not start with '%s'

**Level:** *error*

**Tokens:**
- `A`
- `An`
- `The`

**Ignore Case:** False

### Rule names should avoid weak works like '%s'

**Level:** *error*

[Link](https://developers.google.com/tech-writing/one/clear-sentences)

**Tokens:**
- `was`
- `were`
- `is`
- `are`

**Ignore Case:** True

### Rule names should use sentence case

**Level:** *error*

**Exceptions:**
- `OverlayFS`
- `DNS`
- `TXT`
- `Kubernetes`

### New Value rules should use '%s' instead of '%s'

**Level:** *error*

**Swap:**
- `unrecognized` -> `unfamiliar`
- `unusual` -> `unfamiliar`
- `new` -> `unfamiliar`

**Ignore Case:** True

### Rule names should not be longer than 10 words

**Level:** *error*

**Ignore Case:** False

