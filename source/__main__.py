from crewai import Crew
import market_agents
import market_tasks

def main():

    crew = Crew(
        tasks = [
            market_tasks.research,
            market_tasks.technical_analysis,
            market_tasks.financial_analysis,
            market_tasks.investment_recommendation
        ],
        agents = [
            market_agents.researcher,
            market_agents.technical_analyst,
            market_agents.financial_analyst,
            market_agents.hedge_fund_manager
        ],
    verbose=2,
    )

    result = crew.kickoff(
        inputs={
            'company':'Apple'
        }
    )

if __name__ == "__main__":
    main()