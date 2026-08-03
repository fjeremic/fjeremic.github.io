---
title: Last Man Standing League
date: 2026-01-01
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

The goal of this league is for there to be the Last Man Standing. Players are evicted from the league based on their
performance as we progress through the season. The season will be split into two half-seasons of equal length:

|                            | Game Weeks (inclusive) | # Of Weeks In Half-Season |
|:--------------------------:|:----------------------:|:-------------------------:|
| 1<sup>st</sup> half-season | GW1 - GW19             | 19                        |
| 2<sup>nd</sup> half-season | GW20 - GW38            | 19                        |

For each half-season:

1. The player with the lowest score of the GW according to the FPL league scoring rules gets eliminated from the league.
In case of a tie the player with the smaller overall score gets eliminated. In case of further ties a coin flip is done
for who gets eliminated.
2. If there are more than 18 players in the league then 2 players will be eliminated each week until the number of
players left in the league is 1 more than the number of GWs left in the half-season. At that point we revert back to
eliminating a single player each week.
3. If there are less than 18 players in the league then no players is evicted until the number of players in the league
is 1 more than the number of GWs left in the half-season. At that point we begin eliminating a single player each week.


### Payout Structure

The pot will be split halfway, with the winner of each half-season receiving 50% of the pot.

|                                   | Payout     | Winner                               |
|:---------------------------------:|:----------:| ------------------------------------:|
| 1<sup>st</sup> half-season winner | 50% of pot |                                      |
| 2<sup>nd</sup> half-season winner | 50% of pot |                                      |

### Payment

Payments can only be made via [Interac e-Transfer](https://interac.ca/en/interac-e-transfer-consumer.html) to 
<a href="mailto:{{< fpl-get-data "lms" "eTransferEmail" >}}">{{< fpl-get-data "lms" "eTransferEmail" >}}</a>.
Please send **{{< fpl-get-data "lms" "eTransferAmount" >}}** by {{< fpl-get-data "lms" "joinDeadline" >}} and
include your Team name and Manager name in the description of the Interac e-Transfer.

{{< fpl-payment-table "lms" >}}
