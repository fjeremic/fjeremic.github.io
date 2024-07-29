---
title: Last Man Standing League
date: 2024-01-01
showDate: false
showAuthor: false
showEdit: false
showReadingTime: false
showTableOfContents: true
sharingLinks: false
---

<br>

{{< alert >}}
Click/tap to [auto-join]({{< fpl-get-data "lms" "joinLink" >}}) or see [all leagues](../)
{{< /alert >}}

## Rules

The league and the players enrolled must abide by the following rules:

1. Maximum number of players is &#8734;
2. Scoring system is identical to the official [Fantasy Premier League](https://fantasy.premierleague.com/help/rules)
with slight modifications explained below.
3. Payments are to be made by **{{< fpl-get-data "lms" "joinDeadline" >}}** or you risk eviction from the league.
See the [Payment](#payment) for more details.

### Scoring System

The goal of this league is for there to be one Last Man Standing in GW38. This means players are evicted from the league
based on their performance as we progress through the season.

1. The player with the lowest score of the GW according to the FPL league scoring rules gets eliminated from the league.
In case of a tie the player with the smaller overall score gets eliminated. In case of further ties a coin flip is done
for who gets eliminated.
2. If there are more than 39 players in the league then 2 players will be eliminated each week until the number of
players left in the league is 1 more than the number of GWs left in the season. At that point we revert back to
eliminating a single player each week.
3. If there are less than 39 players in the league then no players is evicted until the number of players in the league
is 1 more than the number of GWs left in the season. At that point we begin eliminating a single player each week.


### Payout Structure

The following payout structure will be used to distribute the funds collected on the last day of the current Fantasy
Premier League season:

|                   | Payout       | 
|:-----------------:|:------------:|
| Last Man Standing | 70% of pot   |
| Runner-up         | 30% of pot   |

### Payment

Payments can only be made via [Interac e-Transfer](https://interac.ca/en/interac-e-transfer-consumer.html) to 
<a href="mailto:{{< fpl-get-data "lms" "eTransferEmail" >}}">{{< fpl-get-data "lms" "eTransferEmail" >}}</a>.
Please send **{{< fpl-get-data "lms" "eTransferAmount" >}}** by {{< fpl-get-data "lms" "joinDeadline" >}} and
include your Team name and Manager name in the description of the Interac e-Transfer.

{{< fpl-payment-table "lms" >}}
