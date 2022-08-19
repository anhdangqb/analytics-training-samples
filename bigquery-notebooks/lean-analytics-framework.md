# Analytics Framework

Analytics Framework starts with designing set of metrics to measure different aspects of business. Ideally, set of metrics should reflect, and so be mappable with components of business.

Read more: [Recap from Lean Analytics](https://publish.obsidian.md/danghuynhmaianh/00-Work/Lean-Analytics/Tutorials/5-Analytics+Frameworks) - Pass: `danghuynhmaianh`


### Decompose business elements
Introduce 2 common model to map business elements with set of metrics


#### Pirate Metrics
- This framework is designed to measure 5 elements of a successul business: Impression -> Click -> Install -> Generate Revenue -> Viral
- **AARRR**: Acquisitions, Activation, Retention, Revenue, Referral

For each elemen, we have relevant metrics:

| Element     | Function                                                                                                                                        | Relevant metrics                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Acquisition | Generate attention of customers through a variety of means (organic, marketing)                                                                 | Traffic, mentioned, cost per click, search results, cost of acquisition, open rate         |
| Activation  | Turn the resulting drive-by visitors into users who are somehow activated (Activated: Any milestones that customers start to realize the value) | Enrollments, sign-ups, completed onboarding steps, use product at least one, subscriptions |
| Retention   | Convince users to come back repeatedly                                                                                                          | Engagement, time since last visit, DAU/MAU, churns                                         |
| Revenue     | Business outcomes: $$, ad clicks, content creation, purchases, etc.                                                                             | CLV, Conversion rate, shopping cart size, Ad revenue                                       |
| Referral    | Viral and word-of-mouth                                                                                                                         | Invites sent, viral coefficient, viral cycle time, organic uplift                          |

#### Three engines of growth

3 engines that drive the growth of a start-up -> Associated with `Key Performance Indicators` (KPIs)

1.  `Sticky Engine`: getting users to return, keep using your products  
    - Not sticky -> churn will be high, low engagement -> Engagement is the key: Facebook's early user counts weren't huge, but the stickiness is off charts. Hard for people to leave Gmail or Evernote -> All data there  
    - Customer Retention  
    - Churn rate  
    - Usage Frequency (not only about retention)
2.  `Virality`: getting the word out, compounds (organic factor)  
    - Viral coeffiecient: the number of new users that each user brings on (similar of `k-factor` - `o/p = organic users/paid users`)  
    - _Measure the actions_ that make up the cycle : ask to connect to email account, invite other contacts, take actions -> Distinct Stages contribute to the Virality  
    - By measure actions, we can twist the viral engine (changing the message, simplifying the signup process)  
    - `Viral Cycle time` & `Type of Virality`  
    - Growth: Virality > 1 (also have churn and loss)
3.  `Paid Engine`: Usually premature to turn this engine on before you know that your product is sticky and viral


### Time-based 

All the metrics above is varied by:

- Definition of "snapshot": means that the calculation could be aggregated over different time windows 7 days, 30 days, 60 days
- Definition of "granualrity": All-together, by product code, by geo code, etc.

### Sequential-based

We also care about the natural sequence of metrics

- **Leading metrics**: The metrics "happen" before (inform as the causes, or early warnings/indicators). People also call them "actionable" metrics, as at the moment we see the metrics we can still take some actions
- **Lagging metrics**: The metrics "follow" after (inform the consequence). At the moment we see the metrics, it's too late for any action, things happened

> For example, complaint rate is leading metric. Churn rate is lagging metric.