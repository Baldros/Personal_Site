import os
from langchain.tools import tool
from ai_agent.functions import *
from pydantic import BaseModel, Field
from typing import Optional, List


# Environment Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_PATH = os.path.join(BASE_DIR, "Context", "files")

# ======================================================
# Tool Input Schemas
# ======================================================
class SendEmailInput(BaseModel):
    """Input schema for the send_email tool."""
    subject: str = Field(
        description="The subject of the email. Keep it concise and relevant."
    )
    body: str = Field(
        description="The main content of the email. Explain the request or information clearly."
    )
    attachments: Optional[List[str]] = Field(
        default=None,
        description="Optional. List of absolute file paths to attach to the email."
    )
    is_html: bool = Field(
        default=False,
        description="Optional. Set to True if the body is HTML content. Default is False (plain text)."
    )


class TableAnalysisInput(BaseModel):
    """Input schema for the analyze_table tool."""
    file_path: str = Field(
        description="Absolute path to the CSV or Excel file to be analyzed."
    )
    operation: str = Field(
        description=(
            "Type of operation to perform. Options: "
            "'list_categories' - Lists all unique values in a column. "
            "'get_element' - Retrieves a specific value from a target column based on a search condition."
        )
    )
    column_name: str = Field(
        description=(
            "Name of the column to search or filter by. "
            "For 'list_categories': the column to extract unique values from. "
            "For 'get_element': the column to match against search_value."
        )
    )
    target_column: Optional[str] = Field(
        default=None,
        description=(
            "Required only for 'get_element' operation. "
            "The column from which to retrieve the value after finding a match."
        )
    )
    search_value: Optional[str] = Field(
        default=None,
        description=(
            "Required only for 'get_element' operation. "
            "The value to search for in the column_name to find the matching row."
        )
    )


# ======================================================
# Portfolio Tools (About André)
# ======================================================

@tool(
    "get_professional_experience",
    return_direct=False,
    description=(
        "Retrieves André Amorim's detailed professional experience history. "
        "Use this tool to answer questions about: "
        "- Past jobs, roles, and positions held "
        "- Companies worked for and employment periods "
        "- Key responsibilities and achievements "
        "- Career progression and timeline "
        "WHEN TO USE: Any query about work history, employment, or professional background."
    )
)
def get_professional_experience() -> str:
    """Retrieves André Amorim's professional experience from file."""
    return read_md_content(os.path.join(FILES_PATH, "ProfessionalExperience.md"))


@tool(
    "get_academic_background",
    return_direct=False,
    description=(
        "Retrieves André Amorim's academic background and education details. "
        "Use this tool to answer questions about: "
        "- University degrees and certifications "
        "- Educational institutions attended "
        "- Academic research and publications "
        "- Study areas and specializations "
        "WHEN TO USE: Any query about education, academic credentials, or research work."
    )
)
def get_academic_background() -> str:
    """Retrieves André Amorim's academic background from file."""
    return read_md_content(os.path.join(FILES_PATH, "AcademicBackgound.md"))


@tool(
    "get_technical_skills",
    return_direct=False,
    description=(
        "Retrieves the comprehensive list of André Amorim's technical skills and technologies. "
        "Use this tool to answer questions about: "
        "- Programming languages proficiency "
        "- Frameworks and libraries expertise "
        "- Tools and platforms knowledge "
        "- Technical competencies and certifications "
        "WHEN TO USE: Any query about specific technologies, skills, or technical capabilities."
    )
)
def get_technical_skills() -> str:
    """Retrieves André Amorim's technical skills from file."""
    return read_md_content(os.path.join(FILES_PATH, "TechinalSkill.md"))


@tool(
    "get_contact_info",
    return_direct=False,
    description=(
        "Retrieves André Amorim's contact information and social media links. "
        "Use this tool to get: "
        "- Email addresses "
        "- Phone numbers "
        "- LinkedIn profile "
        "- GitHub and other professional social links "
        "WHEN TO USE: When someone asks how to reach or connect with André."
    )
)
def get_contact_info() -> str:
    """Retrieves André Amorim's contact information from file."""
    return read_md_content(os.path.join(FILES_PATH, "Contact.md"))


@tool(
    "get_executive_summary",
    return_direct=False,
    description=(
        "Retrieves a high-level professional summary of André Amorim. "
        "Use this tool for: "
        "- Quick overview of career highlights "
        "- Professional introduction and elevator pitch "
        "- Summary of key expertise areas "
        "- General career trajectory "
        "WHEN TO USE: When someone asks 'Who is André?' or needs a general professional overview."
    )
)
def get_executive_summary() -> str:
    """Retrieves André Amorim's executive summary from file."""
    return read_md_content(os.path.join(FILES_PATH, "ExecutiveSummary.md"))


# ======================================================
# Product Tools (About Atlas Desktop)
# ======================================================

@tool(
    "get_atlas_product_info",
    return_direct=False,
    description=(
        "Retrieves comprehensive information about the 'Atlas Desktop' product. "
        "⚠️ ESSENTIAL TOOL for product-related queries. "
        "Use this tool to answer questions about: "
        "- What Atlas Desktop is and how it works "
        "- Product features and capabilities "
        "- Use cases and applications "
        "- Technical specifications "
        "- Platform details (desktop app characteristics) "
        "- Benefits and value proposition "
        "WHEN TO USE: Any query containing 'Atlas', product questions, or feature inquiries. "
        "This is the PRIMARY source for product sales and explanations."
    )
)
def get_atlas_product_info() -> str:
    """Retrieves Atlas Desktop product information from file."""
    return read_md_content(os.path.join(FILES_PATH, "AssistentDesktopDescription.md"))


@tool(
    "get_agent_capabilities",
    return_direct=False,
    description=(
        "Retrieves a detailed list of the Atlas Agent's specific capabilities. "
        "Use this tool to answer questions about: "
        "- Specific automation tasks the agent can perform "
        "- Agent's technical capabilities and limitations "
        "- Detailed feature breakdown "
        "- Integration capabilities "
        "WHEN TO USE: When users ask about what the agent can DO specifically, "
        "or need granular details beyond the general product overview."
    )
)
def get_agent_capabilities() -> str:
    """Retrieves Atlas Agent capabilities from file."""
    return read_md_content(os.path.join(FILES_PATH, "CAPACIDADES_DO_AGENTE.md"))


# ======================================================
# Data Analysis Tools
# ======================================================

@tool(
    "analyze_table",
    args_schema=TableAnalysisInput,
    return_direct=False,
    description=(
        "Analyzes tabular data from CSV or Excel files to extract specific information. "
        "SUPPORTED OPERATIONS: "
        "1. 'list_categories' - Extracts all unique values from a specified column "
        "   Example: Find all unique product categories, customer types, or status values "
        "2. 'get_element' - Retrieves a specific cell value based on a search condition "
        "   Example: Get the price for product X, find email for customer Y "
        "WHEN TO USE: "
        "- Extracting unique categories or lists from data "
        "- Looking up specific values in spreadsheets "
        "- Filtering and searching tabular data "
        "REQUIRED: file_path, operation, column_name "
        "OPTIONAL: target_column and search_value (required for 'get_element')"
    )
)
def analyze_table(
    file_path: str, 
    operation: str, 
    column_name: str, 
    target_column: Optional[str] = None, 
    search_value: Optional[str] = None
) -> str:
    """
    Analyzes tabular data (CSV/Excel) to extract specific information.
    Supports listing unique categories or retrieving specific element values.
    """
    try:
        df = load_dataframe(file_path)
        
        if operation == "list_categories":
            categories = list_categories(df, column_name)
            return f"Unique values in '{column_name}': {categories}"
            
        elif operation == "get_element":
            if not target_column or not search_value:
                return "Error: 'target_column' and 'search_value' are required for 'get_element' operation."
            
            result = get_element(df, search_value, column_name, target_column)
            return f"Value in '{target_column}' where '{column_name}' is '{search_value}': {result}"
        
        return "Error: Invalid operation. Use 'list_categories' or 'get_element'."
    
    except Exception as e:
        return f"Error processing table: {str(e)}"


# ======================================================
# Communication Tools
# ======================================================

@tool(
    "send_email",
    args_schema=SendEmailInput,
    return_direct=False,
    description=(
        "Sends an email to André Amorim, the system manager and owner. "
        "⚠️ CRITICAL COMMUNICATION TOOL "
        "Use this tool to: "
        "- Forward user requests that require human attention "
        "- Report issues, bugs, or system problems "
        "- Escalate complex queries beyond agent capabilities "
        "- Send information, summaries, or reports to André "
        "- Request clarifications or additional resources "
        "BEST PRACTICES: "
        "- Write clear, professional subject lines "
        "- Provide complete context in the body "
        "- Include relevant details the user shared "
        "- Attach files when necessary using absolute paths "
        "- Use HTML format for rich content (tables, formatting) "
        "REQUIRED: subject, body "
        "OPTIONAL: attachments (list of file paths), is_html (boolean)"
    )
)
def send_email(
    subject: str,
    body: str,
    attachments: Optional[List[str]] = None,
    is_html: bool = False
) -> str:
    """Send an email using Gmail and SMTP."""
    return send_email_logic(
        assunto=subject,
        corpo=body,
        anexos=attachments,
        html=is_html
    )


@tool(
    "list_baldros_repos",
    return_direct=False,
    description=(
        "Lists all public repositories from Baldros (André Amorim) GitHub profile. "
        "🎯 PRIMARY REPOSITORY DISCOVERY TOOL "
        "Use this tool FIRST when you need to: "
        "- Find which repository is most relevant to answer a recruiter's question "
        "- Identify projects related to specific technologies, frameworks, or topics "
        "- Get an overview of André's technical portfolio before diving into specific repos "
        "- Compare multiple projects to determine which one best matches the inquiry "
        "- Locate repositories by name, description, or technical domain "
        ""
        "WHEN TO USE: "
        "- Recruiter asks about specific technologies (e.g., 'Do you have React projects?') "
        "- Questions about project types (e.g., 'What APIs have you built?') "
        "- Need to find the most relevant repository before fetching detailed code "
        "- General portfolio questions (e.g., 'What are your main projects?') "
        "- Before using GitHub MCP tools - use this to identify target repositories first "
        ""
        "PRIORITY: Use this tool BEFORE GitHub MCP when you need repository discovery. "
        "This tool provides a complete, fast overview of all repositories at once, "
        "making it easier to identify which specific repo to investigate further. "
        ""
        "OUTPUT: Returns formatted list with repository names, descriptions, and URLs. "
        "Use the repository names from this output to then fetch specific files or details "
        "using other GitHub tools if needed."
    )
)
def list_baldros_repos() -> str:
    """
    Busca todos os repositórios públicos do usuário Baldros.
    
    Returns:
        Lista formatada com informações dos repositórios
    """
    # Get Repos:
    repos = get_baldros_repos()
    
    # Format Repos:
    repos_str = f"📚 Total de {len(repos)} repositórios encontrados:\n\n"
    
    for repo in repos:
        name = repo["name"]
        desc = repo.get("description", "Sem descrição")
        url = repo["html_url"]
        language = repo.get("language", "N/A")
        updated = repo.get("updated_at", "N/A")
        
        repos_str += f"• **{name}** ({language})\n"
        repos_str += f"  📝 {desc}\n"
        repos_str += f"  🔗 {url}\n"
        repos_str += f"  📅 Última atualização: {updated}\n\n"
        
    return repos_str


# ======================================================
# Tool Registry
# ======================================================

# Export all tools for easy import
LOCAL_TOOLS = [
    get_professional_experience,
    get_academic_background,
    get_technical_skills,
    get_contact_info,
    get_executive_summary,
    get_atlas_product_info,
    get_agent_capabilities,
    analyze_table,
    send_email,
    list_baldros_repos
]
