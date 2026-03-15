# Talking Points — Kendrick Sin

## The 1200% YoY Revenue Growth Story (Alibaba Cloud ISV, 2021–2023)

Kendrick joined a Chinese technology ISV as Regional BD / Product Manager tasked with expanding its software products into Southeast Asia — a market the company had no prior presence in. He led the entire product lifecycle: market entry planning, localisation, customer acquisition, and deal closing.

Within 8 months he drove successful launches in 3 countries. He implemented Agile methodology into the product development process and aligned the roadmap directly to requirements gathered from prospective customers, which drove a 300% increase in software uptake in the local market. By the end of his two-year tenure, he had closed deals with 5 major clients, resulting in 1200% year-over-year revenue growth.

The key lesson: in a new market, product-market fit is not given — it has to be engineered through deep customer discovery and the willingness to reshape the product around what local customers actually need. Kendrick also learned to balance lean operating costs against project revenue expectations, giving him early exposure to the economics of a startup-stage international expansion.


## The Qwen Ecosystem Open-Source Project

Kendrick authored and maintains an open-source repository ([github.com/kendricksin/learn_to_qwen](https://github.com/kendricksin/learn_to_qwen)) designed to lower the barrier to AI adoption for non-technical stakeholders — particularly in the Southeast Asian developer community around the Qwen AI ecosystem.

The motivation was straightforward: Kendrick was seeing enterprise clients struggle to evaluate or adopt Qwen-based AI not because the technology lacked capability, but because the available documentation assumed a level of technical sophistication that most business-side users did not have. The repository addresses that gap with practical, accessible implementation guides and examples.

He also scaled the local developer community around Qwen in Thailand as part of his role at Alibaba Cloud, running developer education initiatives and acting as a local technical evangelist for the ecosystem.


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

## POC Delivery Stories (Alibaba Cloud Thailand, 2023–present)

Kendrick has led multiple high-stakes Proof of Concept engagements for enterprise clients across Thailand and Southeast Asia, bridging the gap between complex AI capabilities and demonstrable business ROI.

Kendrick was also the leading designer of a large retail conglomorate MOU scope, negotiating resources, getting stakeholder buy in, all the way down to listing the broad use cases, to pratical solutions, getting the right experts to join individual workshops. 

The pattern for a successful POC: start with a tightly scoped, high-visibility workflow problem where the outcome is measurable and the stakeholder has genuine skin in the game. POCs that stall typically do so because the problem was too vague, the champion was too junior to drive internal buy-in, or the success criteria were not agreed upfront.


## The Bug Fix Story (AI Product Suite)

While working as a forward-deployed business development manager at Alibaba Cloud Thailand, Kendrick proactively tested and discovered bugs before they were released to customers, within the AI product suite. Fixing these discrepencies prevented poor customer experience post sales.

This was a great example of how forward deployed technical Business Developments can speed up product market fit, and prevent painful misalignment that could last years before getting fixed.
