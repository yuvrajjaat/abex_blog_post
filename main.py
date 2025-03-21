"""
main.py

This is the main driver script for the multi-agent SEO blog generator.
It orchestrates the execution of each agent in sequence.
"""

from agents import ResearchAgent, ContentPlanningAgent, ContentGenerationAgent, SEOOptimizationAgent, ReviewAgent

def main():
    # Step 1: Research
    research_agent = ResearchAgent(api_key="b2e16dfd3203470bb7c107a818526b86")  # Replace with your NewsAPI key
    research_info = research_agent.research()
    print("Research complete.")
    
    # Step 2: Create Outline
    planning_agent = ContentPlanningAgent()
    outline = planning_agent.create_outline(research_info)
    print("Outline created.")
    
    # Step 3: Generate Content
    generation_agent = ContentGenerationAgent()
    raw_content = generation_agent.generate_content(outline, research_info)
    print("Content generated.")
    
    # Step 4: SEO Optimization
    seo_agent = SEOOptimizationAgent()
    seo_content = seo_agent.optimize_seo(raw_content)
    print("SEO optimization complete.")
    
    # Step 5: Review and Finalize
    review_agent = ReviewAgent()
    final_content = review_agent.review_content(seo_content)
    print("Content review complete.")
    
    # Write the final blog post to a file
    with open("output_blog.txt", "w", encoding="utf-8") as file:
        file.write(final_content)
    print("Final blog post saved to 'output_blog.txt'.")

if __name__ == "__main__":
    main()
