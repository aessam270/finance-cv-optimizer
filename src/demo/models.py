"""
Finance CV Optimizer - Data Models

╔═══════════════════════════════════════════════════════════════════════════════╗
║                           🚨 DEMO ONLY 🚨                                      ║
║                                                                                ║
║  This file contains interface definitions and data models only.               ║
║  It is provided for demonstration purposes to show the structure              ║
║  of the full implementation.                                                  ║
║                                                                                ║
║  The full production-ready implementation is available on Gumroad:            ║
║  https://gumroad.com/l/your-product-link                                      ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

from enum import Enum
from pydantic import BaseModel, Field


class RoleType(str, Enum):
    """
    Supported Finance/Banking role types.
    
    The optimization engine adapts its approach based on the selected role,
    using role-specific keywords, metrics, and industry terminology.
    """
    FINANCE = "finance"
    """General finance roles: Analyst, Controller, Treasury, Accountant"""
    
    CREDIT_ANALYST = "credit_analyst"
    """Credit and lending roles: Credit Analyst, Loan Officer, Underwriter"""
    
    RISK_MANAGER = "risk_manager"
    """Risk and compliance roles: Risk Analyst, Compliance Officer, Auditor"""


class OptimizedCV(BaseModel):
    """
    Structured output from the CV optimization engine.
    
    This model represents the fully optimized CV with:
    - Enhanced professional summary
    - ATS-optimized experience bullets
    - Matched keywords from job description
    - Actionable improvement suggestions
    """
    
    candidate_name: str = Field(
        ...,
        description="Full name of the candidate, preserved exactly as provided"
    )
    
    professional_title: str = Field(
        ...,
        description="Target job title aligned with the job description"
    )
    
    professional_summary: str = Field(
        ...,
        description="3-4 sentence summary highlighting experience, achievements, and value proposition"
    )
    
    experience: list[dict] = Field(
        default_factory=list,
        description="List of work experiences with title, company, period, and bullet points"
    )
    
    skills: dict = Field(
        default_factory=dict,
        description="Categorized skills: core competencies, technical tools, languages"
    )
    
    education: list[str] = Field(
        default_factory=list,
        description="Educational background in standard format"
    )
    
    certifications: list[str] = Field(
        default_factory=list,
        description="Professional certifications with year or status"
    )
    
    ats_score: int = Field(
        ge=0,
        le=100,
        description="Estimated ATS compatibility score (0-100)"
    )
    
    matched_keywords: list[str] = Field(
        default_factory=list,
        description="Keywords from job description found/added to the CV"
    )
    
    suggestions: list[str] = Field(
        default_factory=list,
        description="Actionable recommendations for further improvement"
    )


class OptimizeRequest(BaseModel):
    """
    Request body for the CV optimization endpoint.
    """
    
    cv_text: str = Field(
        ...,
        min_length=50,
        description="Raw CV content (plain text)"
    )
    
    jd_text: str = Field(
        ...,
        min_length=50,
        description="Target job description"
    )
    
    role_type: RoleType = Field(
        default=RoleType.FINANCE,
        description="Target role category for optimization"
    )


class OptimizeResponse(BaseModel):
    """
    Response from the CV optimization endpoint.
    """
    
    success: bool = Field(
        ...,
        description="Whether the optimization completed successfully"
    )
    
    data: OptimizedCV | None = Field(
        default=None,
        description="The optimized CV data (if successful)"
    )
    
    error: str | None = Field(
        default=None,
        description="Error message (if unsuccessful)"
    )
    
    processing_ms: int = Field(
        ...,
        description="Processing time in milliseconds"
    )
