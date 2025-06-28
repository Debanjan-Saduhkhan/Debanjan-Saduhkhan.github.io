{
  "type": "memory_graph",
  "source": "Debanjan_Resume_2025.pdf",
  "nodes": [
    {
      "id": "profile",
      "type": "person",
      "name": "Debanjan Sadhukhan",
      "location": "Bangalore, India",
      "email": "debanjans.sadhukhan@gmail.com",
      "phone": "+91-7896172142",
      "linkedin": "https://www.linkedin.com/in/debanjan-sadhukhan-b4538092/"
    },
    {
      "id": "current_position",
      "type": "experience",
      "role": "Senior Research Scientist",
      "company": "Games24x7",
      "location": "Bangalore, India",
      "start_date": "May 2024",
      "description": "Led a team to convert business problems into research challenges and developed interpretable deep reinforcement learning-based user-ranking method."
    },
    {
      "id": "education_phd",
      "type": "education",
      "degree": "PhD in Computer Science & Engineering",
      "institution": "IIT Guwahati",
      "duration": "2010-2017",
      "thesis": "Stochastic Approach to Quality of Service in Data Gathering for Wireless Sensor Networks"
    },
    {
      "id": "key_skill_rl",
      "type": "skill",
      "label": "Reinforcement Learning"
    },
    {
      "id": "key_skill_causal",
      "type": "skill",
      "label": "Causal Discovery"
    },
    {
      "id": "key_skill_ml",
      "type": "skill",
      "label": "Machine Learning"
    },
    {
      "id": "publication_effectrl",
      "type": "publication",
      "title": "EFfECT-RL: Enabling Framework for Establishing Causality and Triggering Engagement through RL",
      "venue": "ACM CIKM 2024",
      "link": "https://dl.acm.org/doi/abs/10.1145/3627673.3680058"
    },
    {
      "id": "achievement_gate",
      "type": "achievement",
      "title": "Qualified GATE with 97 percentile",
      "year": "2010"
    }
  ],
  "edges": [
    {"from": "profile", "to": "current_position", "relation": "works_at"},
    {"from": "profile", "to": "education_phd", "relation": "studied_at"},
    {"from": "profile", "to": "key_skill_rl", "relation": "has_skill"},
    {"from": "profile", "to": "key_skill_causal", "relation": "has_skill"},
    {"from": "profile", "to": "key_skill_ml", "relation": "has_skill"},
    {"from": "profile", "to": "publication_effectrl", "relation": "authored"},
    {"from": "profile", "to": "achievement_gate", "relation": "achieved"}
  ]
}
