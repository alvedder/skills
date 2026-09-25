# Calibration examples

Read the case matching the current editing decision. Each rewrite uses only supplied facts;
the notes explain the boundary that makes the edit useful.

## Preserve concise text

For a teammate who knows the test suite, source and rewrite are identical:

```text
Deploy failed: auth.test.ts:42 is red.
```

The alert already gives the event and location. A conversational update can also stay as is:

```text
Merged both fixes, everything is green, go ahead and keep building on main.
```

## Move the lede without strengthening it

```text
SOURCE
CPU throttling rose to 18 percent after the afternoon deploy. Sustained
throttling at this level typically correlates with elevated request latency.
A rollback is recommended.

REWRITE
A rollback of the afternoon deploy is recommended. CPU throttling rose to
18 percent, a level that typically correlates with elevated request latency
when sustained.
```

The recommendation leads. The correlation and its sustained-condition qualifier survive.

## Expand supplied context

Request: explain this to a new teammate.

```text
SOURCE
SLO = service-level objective, our target for reliability. SLO missed Tuesday.
Review recommended Friday; owner: Maya.

REWRITE
We missed our service-level objective (SLO), our reliability target, on Tuesday.
A review is recommended for Friday, with Maya as owner.
```

The definition comes from the source. The proposed review remains a recommendation.

## Explain notation without adding analysis

```text
SOURCE
Fund IV: $116M. Fund III: $157M. 21 paying users at $200/mo.

REWRITE
Fund IV is $116M; Fund III is $157M. There are 21 paying users at $200/mo.
```

Names, figures and units retain their form. A request for analysis could justify a computed
total; a readability edit alone does not require one.

## Connect observations without inventing causes

```text
SOURCE
- 95% of arrivals were developers
- Product priced for enterprise buyers
- Last three launches: 4, 3, 0 signups
- Recommend repositioning

REWRITE
Repositioning is recommended. Developers made up 95% of arrivals, while the
product was priced for enterprise buyers. The last three launches brought
4, 3 and 0 signups.
```

The audience and price can be contrasted. Their effect on signups and the developers'
purchasing authority remain unknown.

## Preserve uncertainty and undefined labels

```text
SOURCE
- Competitor A: raised funding, 40 staff, no public pricing
- Competitor B: shut down Q3
- Competitor C: pivoted to services
- Signal strength: medium
- Confidence: L2

REWRITE
Competitor A raised funding, has 40 staff and has no public pricing.
Competitor B shut down in Q3. Competitor C pivoted to services.
The notes rate signal strength as medium and confidence as L2; they do not
define L2.
```

The source gives neither the reason for these outcomes nor its evidence sources. Q3 stays
Q3 because the year and reporting date are unspecified.
