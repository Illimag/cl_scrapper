# Craiglist Gig/Job Operations

This the operation instructions for the Craiglist Gigs/Jobs.

There is a lead generator called "spider".

It is broken up into 3 clusters because it needs to go through 2500 urls every day.

The script goes through each one individually, and because the proxies that are required for the script to run, the service isnt the best.

So there is a cluster that goes through around 800-900 urls each.

So in theory the process should be 3 times as fast.

3 scripts is the maximum currently because the plan is for 40 threads if it goes over then, we cant run the script.

The scripts are run from the user0 system. 
