# BagelAI
### The Agent That Bridges Every Other Agent

> AI is everywhere. But almost nobody knows how to actually use it.

BagelAI is a proactive AI literacy agent delivered as a home screen widget. It lives inside the technology behaviors people already have, meets them where they are, and teaches them to harness AI through doing — not lecturing.

---

## The Problem

- **80%** of companies have deployed AI agents — yet fewer than **1 in 4** have successfully scaled them
- **Half the global workforce** needs AI-specific training to remain effective, and that gap is widening faster than institutions can respond
- **78%** of companies use AI in at least one business function — but only **1%** describe themselves as truly advanced
- The average person has access to more AI capability than any generation in history — and no practical guidance on how to use it

The gap is not intelligence. It is not access. It is the missing bridge between humans and the tools already in their hands.

---

## The Solution

BagelAI is a proactive AI guidance agent that:

- Lives on your **home screen widget** — zero friction, always present
- Identifies what you are trying to accomplish and surfaces the exact AI tool or prompt that solves it
- Teaches through doing — AI literacy is built in context, not in a classroom
- Adapts automatically to your skill level from beginner to advanced
- Functions as a personal AI co-pilot across every app, task, and goal

---

## Core Agent Architecture

### Context Agent
Passively understands what the user is working on and identifies opportunities where AI can help. No input required.

### Guidance Agent
Delivers specific, actionable AI tool and prompt recommendations matched to the user's current task — not generic suggestions.

### Growth Agent
Tracks skill progression over time and evolves recommendations accordingly. Users are never over- or under-served as their capability develops.

---

## Widget Interface

| State | Behavior |
|---|---|
| **Idle** | Displays current AI skill level and a contextual tip |
| **Active** | Surfaces a real-time AI recommendation |
| **Coaching** | Delivers step-by-step guidance for the current task |
| **Quick Action** | Executes a suggested AI task in a single tap |

---

## Target Users

| Segment | Problem BagelAI Solves |
|---|---|
| College students | AI tools exist — practical instruction does not |
| Young professionals | Peers are leveraging AI; they are falling behind |
| Small business owners | No budget for AI consulting; need on-demand expertise |
| Career changers | Must upskill rapidly without access to formal programs |
| General adults | Understand AI matters; lack a clear starting point |

---

## Tech Stack

**Mobile**
- React Native + Expo
- iOS Widget Extension + Android App Widget
- Expo TaskManager
- AsyncStorage

**Agent Layer**
- Node.js runtime
- Anthropic Claude API
- Multi-agent orchestration pipeline: Context → Guidance → Growth
- On-device processing priority

**Backend**
- Supabase — anonymized skill progression metadata only
- No content stored server-side
- No behavioral logging

---

## Roadmap

**Phase 1 — Foundation**
- [ ] Agent architecture and repository structure
- [ ] Widget MVP for iOS and Android
- [ ] Context Agent core logic
- [ ] Tool recommendation engine covering top 20 AI use cases

**Phase 2 — Intelligence**
- [ ] Claude-powered Guidance Agent
- [ ] Skill progression tracking
- [ ] Prompt library with 100+ real-world templates
- [ ] Beta program — 50 users across skill levels

**Phase 3 — Personalization**
- [ ] Adaptive Growth Agent
- [ ] Personalized AI learning paths
- [ ] Productivity app integrations
- [ ] Community prompt sharing

**Phase 4 — Scale**
- [ ] Enterprise and education licensing
- [ ] Third-party API
- [ ] Multilingual support
- [ ] National expansion

---

## Ethical Commitments

- BagelAI does not read user documents, messages, or files
- Skill progression data remains on-device unless the user opts into sync
- Core guidance features are permanently free
- BagelAI amplifies human capability — it does not replace human judgment
- Every recommendation includes a transparent explanation of why it was surfaced

---

## Contact

**Caitlin Przywara** — Founder  
Email: isabellacaitlin03@gmail.com  
LinkedIn: linkedin.com/in/caitlinprzywara  
GitHub: @Isap31

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
