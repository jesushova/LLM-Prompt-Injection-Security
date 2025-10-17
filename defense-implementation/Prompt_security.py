# Prompt Security Module 

"""
Prompt Injection Defense Module
Implements LLM Guard for securing LLM applications
Author: OSEI
Date: October 2025
"""

def allowed_prompt(prompt):
    """
    Security control using LLM Guard to detect prompt injections
    
    Args:
        prompt (str): User input to validate
        
    Returns:
        bool: True if safe, False if injection detected
    """
    from llm_guard.input_scanners import PromptInjection
    from llm_guard.input_scanners.prompt_injection import MatchType
    
    try:
        # Initialize scanner with recommended settings
        scanner = PromptInjection(
            threshold=0.5,
            match_type=MatchType.FULL
        )
        
        # Scan for injection attempts
        sanitized_prompt, is_valid, risk_score = scanner.scan(prompt)
        
        # Log detection events
        if not is_valid:
            print(f"[Security] Injection detected! Risk score: {risk_score:.2f}")
        
        return is_valid
        
    except Exception as e:
        # Fail-safe: reject on error
        print(f"[Security] Scanner error: {str(e)}")
        return False