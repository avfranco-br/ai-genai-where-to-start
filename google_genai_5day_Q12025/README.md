# Use Case and Innovation

> **Background**
- The **Architecture Demand Planning** use-case is the latest as part of my exploration journey started about two years ago on how Generative AI impacts Business, Enterprise, and Solution Architectures.<br>

> **Problem Statement**
    - Increased risk, effort, and cost, caused by inadequate process to allocate architects to projects<br>
      
> **Opportunity**
    - Provide project resource estimation for architecture work based on business requirements, skillset, architects allocation, and any other relevant information to enable successful project solution delivery.<br>

> **How GenAI help to solve**
    - Enabling actionable insights to Project Management Office and Enterprise Architecture teams matching initiatives with architects profile.
    - Enhance overall allocation process informing the decision make process
    - Accelerate assessment of best man to the work
    - Increase process efficiency with focus on insight-driven
    - Promote better collaboration between both teams<br>

# **Enterprise Architecture in the Era of Generative AI**

> **Novel** 
    - Democratise enterprise architecture, embracing the power of Generative AI models, transforming traditional IT landscapes into conversational domains enhancing overal Architecture Capability to empower individuals with knowledge, increase efficiency and productivity, accelerate Business Requirement identification and translation to target reference architectures, improve agility, increase collaboration, cost optimisation, enable business growth, and last not least unlock individual potential.<br><br>

- `Trigger`: How disruptive may Generative AI be for Enterprise Architecture Capability (People, Process and Tools)?
- `Motivation`: Master GenAI while disrupting Enterprise Architecture to empower individuals and organisations with ability to harness EA value and make people lives better, safer and more efficient.
- `Ability`: Exploit my carrer background and skillset across system development, business accumen, innovation and architecture to accelerate GenAI exploration while learning new things.

> **Benefits**
- `Empower individuals with Knowledge`: understand and talk about Business and Technology strategy, IT landscape, Architectue Artefacts in a single click of button.
- `Increase efficiency and productivity`: generate a documented architecture with diagram, model and descriptions. Accelerate Business Requirement identification and translation to Target Reference Architecture. Automated steps and reduced times for task execution.
- `Improve agility`: plan, execute, review and iterate over EA inputs and outputs. Increase the ability to adapt, transform and execute at pace and scale in response to changes in strategy, threats and opportunities.
- `Increase collaboration`: democratise architecture work and knowledge with anyone using natural language.
- `Cost optimisation`: intelligent allocation of architects time for valuable business tasks.
- `Business Growth`: create / re-use of (new) products and services, and people experience enhancements.
- `Resilience`: assess solution are secured by design, poses any risk and how to mitigate, apply best-practices.

> **Aditional Information**
- To learn more head to my HuggingFace space [Talk to your Multi-Agentic Architect Partner](https://huggingface.co/spaces/avfranco/ea4all_agentic_system)<br>

# **Architecture Solution**
> **High-Level Design**<br><br>
**![Architect Demand Management Solution Design](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F17474692%2Ffaf08072c50685f22337b006f073995c%2Fea4all-demand-planning-architecture-design.png?generation=1745165211247666&alt=media)**
<br><br>
**Key Components**
* Data Sources (CSV, Dataframe, SQLite)
* Model and Embeddings (Google Gemini-2.0-flash and text-embedding-004)
* Agentic Tools (RAG and SQL LLM)
* Agentic Framework (CrewAI)
<br>

> **Retrieval augmented generation (RAG) Portfolio Custom Tool**<br>

* **Expertise**: Perform semantic searchs on project portfolio CSV file.</n>
* **Input**: Porfolio question, example, "List all projects with similar architecture requirements."
* **GenAI Capabilities**
  * Structured output/JSON mode
  * Few-shot prompting
  * Retrieval augmented generation (RAG)
  * Vector search/vector store/vector database

> > **Adding metadata to a collection enhance quality response**
```
for index, row in pmo_df.iterrows():
    output_str = ""
    # Treat each row as a separate chunk
    for col in pmo_df.columns:
        output_str += f"{col}: {row[col]},\n"
    _embeddings.append(embeddings_fn.embed_query(output_str))
    _docs.append(output_str)
    _metadatas.append(
        {
            "project_name": row['Project Name'],
            "lob": row['Line of Business'],
            "business_problem": row['Problem Statement'],
            "status": row['Status'],
            "planned-start": row['Timeline - Start'],
            "planned-end": row['Timeline - End'],
            "architect": row['Architect'],
        },
    )
    _ids.append(f"id{index}")
```


> **SQLite Portfolio Custom Tool**<br>

* **Expertise**: Transform Text to SQL statement and query execution on the project portfolio SQLite database.</n>
* **Input**
  * Text: Porfolio question, example, "List all projects with no architect assigned"
  * SQL Query: select * from table where architect is NULL</n>
* **GenAI Capabilities**
  * Function Calling
  * Structured output/JSON mode
  * Few-shot prompting
  * Text to SQL search

> > **Retrieving consistent results using structured-output**
```
#Define the Tool structured-output model
class ProjectDetails(BaseModel):
    """Project Information"""
    project_name: str = Field(description="Project name.")
    project_lob: str = Field(description="Responsible line of business")
    business_problem: str = Field(description="Business problem description.")
    project_status: str = Field(description="Project status")
    planned_start: Optional[str] = Field(default=None, description="Project planned start date")
    planned_end: Optional[str] = Field(default=None,description="Project planned end date")

class ProjectList(BaseModel):
    """List of Projects"""
    projects: List[ProjectDetails] = Field(...,description="List of projects")

#Add structured query to user's question
structured_query = """
    Retrieve project details with these exact requirements:
    - Return a JSON array of project objects
    - Each object must have these EXACT keys:
    1. "project_name"
    2. "project_lob"
    3. "business_problem"
    4. "project_status"
    5. "planned_start"
    6. "planned_end"
    - You must always return valid JSON fenced by a markdown code block. Do not return any additional text.
    - Do NOT fabricate data
    - If no data matches, return an empty array"""
```

> **Architecture Demand Management Agentic System**<br>

* **Expertise**:
  * Retrieve initiative details from the project portfolio
  * Extract skills, experience, education, and architecture requirements
  * Find the most appropriate Architects to do the job
  * Summarise a report with recommendation<br><br>
* **Input**: Porfolio question, example, "List all projects with no architect assigned"<br><br>
* **GenAI Capabilities**
  * Agents
  * Structured output/JSON mode/controlled generation
  * Few-shot prompting
  * Function Calling
  * Text to SQL search
  * Embeddings
  * Retrieval augmented generation (RAG)
  * Vector search/vector store/vector database

> > **Running the Agents in a sequence**
```
   pmo_crew = Crew(
        agents=[search_pmo, parse_project, architect_candidate, resource_advisor],
        tasks=[search_pmo_task, parse_project_task, architect_candidate_task, resource_advisor_task],
        process=Process.sequential,
        verbose=VERBOSE,
        llm=crew_model,
    )
```

> **Conclusion**

* Generative AI can dramatically improve how Architecture delivers value, increase architect's efficiency, promote more collaboration, better experience, and enhancing overall transparency.
