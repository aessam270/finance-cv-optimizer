"""
Finance CV Optimizer - Interface Definitions

╔═══════════════════════════════════════════════════════════════════════════════╗
║                           🚨 DEMO ONLY 🚨                                      ║
║                                                                                ║
║  This file contains interface stubs only. These classes demonstrate           ║
║  the API structure but are NOT functional implementations.                    ║
║                                                                                ║
║  All methods raise NotImplementedError.                                       ║
║                                                                                ║
║  The full production-ready implementation is available on Gumroad:            ║
║  https://assam3.gumroad.com/                                      ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

from abc import ABC, abstractmethod
from .models import OptimizedCV, RoleType


class BaseCVAgent(ABC):
    """
    Abstract base class for CV optimization agents.
    
    This interface defines the contract that any CV optimization
    engine must implement.
    
    Example usage (with full implementation):
    
        agent = FinanceCVAgent(api_key="your-key")
        result = await agent.optimize(
            cv_text="Your CV content...",
            jd_text="Job description...",
            role_type=RoleType.CREDIT_ANALYST
        )
        print(result.ats_score)
    """
    
    @abstractmethod
    async def optimize(
        self,
        cv_text: str,
        jd_text: str,
        role_type: RoleType,
    ) -> OptimizedCV:
        """
        Optimize a CV for a specific job description and role.
        
        Args:
            cv_text: Raw CV content as plain text
            jd_text: Target job description
            role_type: The role category (finance, credit_analyst, risk_manager)
            
        Returns:
            OptimizedCV with structured, ATS-optimized content
            
        Raises:
            ValueError: If CV or JD text is too short
            APIError: If the AI provider is unavailable
        """
        raise NotImplementedError(
            "This is a demo interface. "
            "Get the full implementation at https://assam3.gumroad.com/"
        )


class FinanceCVAgent(BaseCVAgent):
    """
    Finance & Banking CV Optimization Agent.
    
    Specialized agent for optimizing CVs targeted at Finance and Banking
    roles in the MENA/Egypt job market.
    
    Features (in full implementation):
    - Role-specific optimization (Finance, Credit, Risk)
    - ATS keyword extraction and embedding
    - Banking-specific language enhancement
    - MENA market context (Egyptian banks, CBE regulations, EGP amounts)
    - Quantified achievement generation
    
    ⚠️ This is a stub class. Methods are not implemented.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-4o"):
        """
        Initialize the agent.
        
        Args:
            api_key: OpenAI API key
            model: OpenAI model to use (default: gpt-4o)
        """
        raise NotImplementedError(
            "This is a demo interface. "
            "Get the full implementation at https://assam3.gumroad.com/"
        )
    
    async def optimize(
        self,
        cv_text: str,
        jd_text: str,
        role_type: RoleType = RoleType.FINANCE,
    ) -> OptimizedCV:
        """
        Optimize CV for Finance/Banking role.
        
        Args:
            cv_text: Raw CV content
            jd_text: Target job description
            role_type: finance | credit_analyst | risk_manager
            
        Returns:
            OptimizedCV with structured content including:
            - Enhanced professional summary
            - ATS-optimized bullet points
            - Matched keywords
            - Improvement suggestions
            - ATS score (0-100)
        """
        raise NotImplementedError(
            "This is a demo interface. "
            "Get the full implementation at https://assam3.gumroad.com/"
        )


class PDFGenerator:
    """
    PDF Generation for Optimized CVs.
    
    Converts OptimizedCV JSON output into professionally
    formatted PDF documents.
    
    ⚠️ This is a stub class. Methods are not implemented.
    """
    
    def generate(self, cv: OptimizedCV, output_path: str) -> str:
        """
        Generate a PDF from an optimized CV.
        
        Args:
            cv: OptimizedCV object with structured content
            output_path: Path to save the generated PDF
            
        Returns:
            Path to the generated PDF file
        """
        raise NotImplementedError(
            "PDF generation is only available in the full version. "
            "Get it at https://assam3.gumroad.com/"
        )
