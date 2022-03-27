---
title: Tax Advantageous Reporting of Foreign Employment Income
layout: post
tags: [finance, taxes]
---

In the tech world remote employment positions are becoming more popular in recent years. Given the compensation packages
offered by our neighbours south of the border, it may make financial sense to take on a remote employment opportunity
earning USD while remaining a Canadian resident. For purposes of income tax the Canada Revenue Agency requires that you
report any income in CAD [^1]. However CRA does give some leeway in how you must report the foreign employment income:

> Foreign employment income is income earned outside Canada from a foreign employer. Report this income in Canadian
dollars. Use the Bank of Canada exchange rate in effect on the day you received the income. If the amount was paid at
various times in the year, you can use the average annual rate.

This means that for income tax purposes we can calculate the income tax in Canadian dollars using both the daily
exchange rate and the annual exchange rate and use the lower of the two to report on our income taxes so as to reduce
our total tax owed.

### Example

Consider Fred, a contract worker offering his services to a US based company remotely while residing in Canada for the
duration of the 2018 tax year. The contract between Fred and the US based company dictates the payment schedule for his
services to be a total of $5,000 USD which is deposited (in USD) into a cross-border bank account on the first Friday of
every month.

Let's see what Fred's employment income looks like using the 
[Bank of Canada Daily Exchange Rates](https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/):

| Date       | Income (USD) | Exchange Rate | Income (CAD) |
|:-----------|-------------:|:-------------:|-------------:|
| 2018-01-05 | $5,000.00    | 1.2403        | $6,201.50    |
| 2018-02-02 | $5,000.00    | 1.2380        | $6,190.00    |
| 2018-03-02 | $5,000.00    | 1.2891        | $6,445.50    |
| 2018-04-06 | $5,000.00    | 1.2764        | $6,382.00    |
| 2018-05-04 | $5,000.00    | 1.2861        | $6,430.50    |
| 2018-06-01 | $5,000.00    | 1.2964        | $6,482.00    |
| 2018-07-06 | $5,000.00    | 1.3105        | $6,552.50    |
| 2018-08-03 | $5,000.00    | 1.2983        | $6,491.50    |
| 2018-09-07 | $5,000.00    | 1.3164        | $6,582.00    |
| 2018-10-05 | $5,000.00    | 1.2936        | $6,468.00    |
| 2018-11-02 | $5,000.00    | 1.3105        | $6,552.50    |
| 2018-12-07 | $5,000.00    | 1.3299        | $6,649.50    |
| Total      | $60,000.00   |               | $77,427.50   |

The [Bank of Canada Annual Exchange Rate](https://www.bankofcanada.ca/rates/exchange/annual-average-exchange-rates/)
from USD to CAD in 2018 was 1.2957, which translates Fred's $60,000 USD income to $77,742 CAD. The difference in CAD
denominated income taxes between the annual exchange rate and the daily exchange rate is $314.50 CAD. Choosing to use
the daily exchange rate to report Fred's income for 2018 will save him roughly $100 in income taxes owed based on his
marginal tax rate in the province which he resides.

### A Word of Caution

If the currency fluctuation for a given year is too significant, CRA may not accept using the annual exchange rate, as
per Section 1.6.1 quoted below [^2]. However the meaning of "significantly" is not defined, so tread carefully if the
difference in taxes owed using the above calculations is large.

> 1.6.1 For practical reasons, the CRA may also accept the use of an average of exchange rates over a period of time in
order to convert certain income items.  If exchange rates fluctuate significantly, the use of the average exchange rate
for a period will not generally be accepted. Note that a taxpayer transitioning in or out of income tax reporting using
an elected functional currency must use the Bank of Canada rate as described in ¶1.4 and 1.5 in converting the amounts
required by subsections 261(7) or 261(12) and related provisions.

[^1]: [Line 104 - Foreign employment income](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-104-other-employment-income/line-104-foreign-employment-income.html)
[^2]: [Income Tax Folio S5-F4-C1, Income Tax Reporting Currency](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-5-international-residency/series-5-international-residency-folio-4-foreign-currency/income-tax-folio-s5-f4-c1-income-tax-reporting-currency.html)