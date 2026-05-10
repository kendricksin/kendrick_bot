# Talking Points — Kendrick Sin

## The 1200% YoY Revenue Growth Story (Alibaba Cloud ISV, 2021–2023)

Kendrick joined a Chinese technology ISV as Regional BD / Product Manager tasked with expanding its software products into Southeast Asia — a market the company had no prior presence in. He led the entire product lifecycle: market entry planning, localisation, customer acquisition, and deal closing.

Within 8 months he drove successful launches in 3 countries. He implemented Agile methodology into the product development process and aligned the roadmap directly to requirements gathered from prospective customers, which drove a 300% increase in software uptake in the local market. By the end of his two-year tenure, he had closed deals with 5 major clients, resulting in 1200% year-over-year revenue growth.

The key lesson: in a new market, product-market fit is not given — it has to be engineered through deep customer discovery and the willingness to reshape the product around what local customers actually need. Kendrick also learned to balance lean operating costs against project revenue expectations, giving him early exposure to the economics of a startup-stage international expansion.

### APAC Market Entry Playbook

Through this experience, Kendrick developed a clear-eyed view of what actually drives market entry success in APAC — and it is surprisingly not product quality. Three factors matter more:

1. **Position of authority.** APAC markets depend heavily on referrals and brand credibility. Betting on new entrants is a decision that gets pushed around meeting rooms without resolution. A credible brand or reliable backer breaks through that friction.

2. **Technical support and willingness to customise.** APAC has a shortage of technical staff and process owners with high ownership. Selling to the executive is the easy part. Getting their team to push through implementation, gather feedback for customisation, and maintain a steady iteration loop is extremely difficult — and often leads to abandonment or escalation.

3. **Channel partnerships — the non-negotiable.** Nobody has everything: good brand, good delivery, and good relationships from top to bottom. Channels are the multiplier. But the incentives must be structured correctly from the start. As deals progress and resource constraints get pushed around the negotiation table, incentives dry up and motivations flip quickly. Finding the right partner is a force multiplier; finding the wrong one can end the entire effort.

### Enterprise Deal Structuring

Kendrick's repeatable lesson from driving triple-digit growth: structure the deal well from the start. That means understanding existing gaps in enterprise procurement cycles, mapping the customer's decision process, and carving out strategic "free samples" — scoped tightly enough to backstop the engineering team, but compelling enough that the customer feels confident they will get their money's worth.

The greatest trap in enterprise sales is going into a meeting without a negotiation strategy: no freebie, no price target, and no trade-offs up for bartering.


## Open-Source Developer Community Work

Kendrick has consistently invested in lowering the barrier to AI adoption for non-technical stakeholders through open-source contributions and developer education.

At Alibaba Cloud, he authored and maintained repositories designed to help business-side users evaluate and adopt AI — addressing a gap where available documentation assumed technical sophistication that most users did not have. He ran developer education initiatives and acted as a local technical evangelist for the AI ecosystem in Thailand.

After leaving Alibaba Cloud, that commitment continued. He now maintains [learn_to_vibe](https://github.com/kendricksin/learn_to_vibe) — an open-source repository covering AI-assisted coding from chatbot mode to CLI mode, with a full offline demo for live "vibe coding" sessions. The goal remains the same: give new users a practical, follow-along path to set up their devices and adopt AI-assisted development.

The thread across all of this work: Kendrick believes developer community is built through hands-on, accessible material — not marketing. If someone can follow your repo and get a working result in one sitting, they become an advocate.


## The SAF Innovator-in-Residence Experience

After two years as a Naval Officer, Kendrick was seconded from the Republic of Singapore Navy to the Defence Science and Technology Agency (DSTA) as an Innovator-in-Residence — a role focused on driving technology adoption inside one of Singapore's most structured institutions.

He managed a portfolio of six organisation-scale innovation projects, each valued at up to $5 million. Delivering innovation inside a large bureaucracy meant navigating procurement cycles, risk aversion, and institutional inertia — while still shipping. He maintained a consistent cadence of two Minimum Viable Products delivered bi-annually, with 100% of those MVPs progressing to full implementation. That is an unusually high conversion rate and reflects a discipline around scoping MVPs to solve problems that stakeholders were already committed to solving.

Two highlights stand out:

- **Predictive material provisioning system:** Reduced inventory costs by 30% and improved supply chain efficiency by replacing manual stock management with a data-driven forecasting model.
- **Gamified naval warfare training:** Redesigned trainee engagement through gamification, achieving 300% increase in engagement and introducing structured metric tracking for warfighting performance — something the SAF had not previously had.

The experience shaped Kendrick's view that innovation inside large institutions is fundamentally a change management challenge. The technology is rarely the hard part.

## The Interactive Resume & Kendrick Bot Project

Kendrick built his interactive resume ([kendricksin.github.io/interactive_resume](https://kendricksin.github.io/interactive_resume/)) as both a job-seeking tool and a deliberate portfolio artifact. Rather than submitting a PDF, he wanted to demonstrate AI deployment skills directly — so the resume itself is powered by an AI chatbot.

The bot (this chatbot) is built on FastAPI with a Qwen LLM backend via DashScope, deployed on Render, and embedded into a GitHub Pages site via an iframe. Responses stream token-by-token using Server-Sent Events. The knowledge base is two-tiered: structured resume data in JSON (Tier 1) and richer prose context files (Tier 2) that give the bot nuance beyond what a resume typically conveys.

Key design decisions: no database (conversation history is client-side), strict rate limiting and input sanitisation to prevent abuse, and CORS locked to the resume domain only. The whole stack was built and deployed rapidly using AI-assisted development ("vibe coding").

The project demonstrates that Kendrick does not just talk about AI deployment — he builds with it. It is also a live example of his philosophy: find the workflow where AI does the execution and a human (the recruiter) owns the outcome.

## Post-Sale Account Management Philosophy

Kendrick views post-sale in APAC as an inherently adversarial-cooperative process. If the deal was structured well, there is some margin left to barter when delivery inevitably hits bumps. But it is impossible to prepare for every contingency.

His approach: continuously monitor delivery and track every instance where his company went above and beyond scope. These are negotiation chips. When the customer raises issues, he can present a balanced ledger — not to be combative, but to maintain mutual accountability. The principle is straightforward: in enterprise relationships, you do not give without taking back.

This discipline — maintaining an ongoing "accounting tab" of over-delivery — has repeatedly given Kendrick leverage during difficult post-sale conversations and kept relationships productive rather than one-sided.

## At-Risk Account Recovery

During a migration project at Alibaba Cloud, a customer developed strong intent to terminate and switch to a competing vendor. Kendrick moved quickly, pulling up his running account of every deliverable his team had completed — alongside the areas where the customer's own team had not held up their end of the bargain.

There were genuine shortfalls on both sides, but the balanced accounting reframed the conversation from blame to shared accountability. After months of negotiation, the migration project was dropped — but Kendrick won C-level favour and pivoted the relationship into a different deal, acknowledging honestly that migration was not the right fit at that point in time.

The takeaway: losing a project does not have to mean losing the account. Transparent accountability and the willingness to concede a bad fit can actually strengthen the relationship for the next opportunity.

## POC Delivery Stories (Alibaba Cloud Thailand, 2023–present)

Kendrick has led multiple high-stakes Proof of Concept engagements for enterprise clients across Thailand and Southeast Asia, bridging the gap between complex AI capabilities and demonstrable business ROI.

Kendrick was also the leading designer of a large retail conglomerate MOU scope, negotiating resources, getting stakeholder buy-in, all the way down to listing the broad use cases, to practical solutions, getting the right experts to join individual workshops.

The pattern for a successful POC: start with a tightly scoped, high-visibility workflow problem where the outcome is measurable and the stakeholder has genuine skin in the game. POCs that stall typically do so because the problem was too vague, the champion was too junior to drive internal buy-in, or the success criteria were not agreed upfront.


## The Bug Fix Story (AI Product Suite)

While working as a forward-deployed business development manager at Alibaba Cloud Thailand, Kendrick proactively tested and discovered bugs before they were released to customers, within the AI product suite. Fixing these discrepancies prevented poor customer experience post-sales.

This was a great example of how forward-deployed technical Business Development can speed up product-market fit, and prevent painful misalignment that could last years before getting fixed.
