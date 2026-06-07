# ds-agent-lab

A practical lab of reusable agents, skills, templates, and evals for modern Data Science workflows.

## About the Project
This repository turns repeated Data Science workflows into reusable, agentic components. Rather than rewriting prompts or reinventing the wheel for every analysis, model review, or stakeholder request, `ds-agent-lab` provides version-controlled, extensible, and auditable definitions for AI agents and custom skills. It is designed for Data Scientists who want to use AI agents as reliable, systematic collaborators for recurring workflows.

## Main Goals
- **Make Data Science workflows reusable**: Package common, complex Data Science steps into modular, standard formats.
- **Provide structured agents and skills**: Provide specialized roles (agents) and specific tasks (skills) with defined inputs, outputs, and execution standards.
- **Help Data Scientists scale core workflows**: Review models, design experiments, check data quality, detect leakage, evaluate metrics, and communicate insights.
- **Encourage auditable, versioned, and extensible AI-assisted workflows**: Ensure that AI assistance is versioned, transparent, and structured, avoiding "black box" or ad-hoc prompt engineering.

## Repository Structure
The repository is structured around `.gemini` definitions for agents and skills, ensuring they can be registered, executed, and versioned:

```text
ds-agent-lab/
├── .gemini/
│   ├── agents/
│   │   └── ml-feature-refactorer.md            # Agent: Refactors BigQuery SQL to add ML features safely
│   └── skills/
│       └── sql-dataset-to-google-doc/
│           ├── SKILL.md                         # Skill: Workflows to generate and render dataset documentation
│           └── scripts/
│               └── render_doc.py               # Render script supporting the documentation skill
└── README.md                                    # Project overview
```

## Difference Between Agents and Skills
To build scalable, structured workflows, we distinguish between two core concepts:

- **Agents**: Specialized roles with distinct responsibilities, perspectives, and instructions (e.g., the `Senior ML Data Engineer` defined in `ml-feature-refactorer.md`). Agents understand context, adapt to goals, and interact across multiple steps.
- **Skills**: Reusable workflows or capabilities designed to accomplish a specific, deterministic task (e.g., rendering dataset documentation to a Google Doc). Skills have fixed workflows (such as `SQL file` → `JSON` → `Text` → `Google Doc`) and predictable inputs/outputs.

## Example Use Cases
Here are practical ways to leverage the assets in this lab:

- **Reviewing a machine learning model before production**: Systematically audit high-dimensional pipelines and code paths before deployment.
- **In-place feature engineering**: Automatically and safely add interpretable, leakage-safe features to SQL training queries using the `ml-feature-refactorer` agent.
- **Checking for data leakage**: Run structured checks to ensure that future information does not leak into training features.
- **Summarizing technical results for stakeholders**: Turn a raw SQL pipeline into standard dataset documentation and write it directly to a shared Google Doc via the `sql-dataset-to-google-doc` skill.
- **Designing an A/B test**: Draft complete, statistically sound test plans and power calculations before running a campaign.
- **Evaluating performance metrics**: Run systematic checks for specific target metrics like PR-AUC, lift, recall @ K, and ranking metrics.

## How to Use
Since these agents and skills are defined in standard Markdown and plain-text configuration blocks, they are platform-agnostic:

1. **Browse**: Search the `.gemini/agents` and `.gemini/skills` directories for roles and workflows that match your task.
2. **Adapt**: Copy or reference an agent/skill markdown file and modify the prompt templates, expectations, and intermediate steps to align with your internal databases or tools.
3. **Execute**: Run associated scripts (e.g., `python .gemini/skills/sql-dataset-to-google-doc/scripts/render_doc.py`) or supply the markdown system instructions directly to your LLM framework of choice.

## Design Principles
All components in this repository adhere to strict professional guidelines:
- **Be explicit about assumptions**: Document data sources, training bounds, and modeling trade-offs clearly.
- **Do not invent metrics or results**: Never synthesize performance numbers, tables, or lift charts; only report empirical or actual metrics.
- **Separate facts from recommendations**: Distinguish between hard data findings (e.g., "The metric is calculated over X") and guidance (e.g., "We recommend adding Y feature").
- **Prefer business impact over vanity metrics**: Tie technical validation directly to stakeholder value and decision-making.
- **Make workflows testable and reusable**: Ensure components are modular, verifiable, and can be integrated into CI/CD pipelines.

## Roadmap
We plan to continually expand this lab with more workflows and assets:
- **More Agents**: Experiment designer, data quality sentinel, and leakage detection agent.
- **More Skills**: Feature store integrators, model bias calculators, and automated performance reporting.
- **Templates**: Standard Jupyter notebook validation templates and ML card generators.
- **Evaluation Tasks**: Standard synthetic datasets to benchmark agent performance on data tasks.
- **Example Case Studies**: End-to-end walkthroughs of agent-assisted model deployments.
- **Contribution Guidelines**: Defined guidelines for community contributions.

## Contributing
Contributions are welcome! If you have built an agent, skill, template, or evaluation workflow that has saved you time or improved your modeling process, please feel free to open a PR or submit an issue. We are especially looking for:
- New agent personas
- Deterministic utility skills
- Robust evaluation metrics / benchmark templates
