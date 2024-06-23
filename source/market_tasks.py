# Tasks
from crewai import Task
from market_agents import researcher, technical_analyst, financial_analyst, hedge_fund_manager


research                    = Task(
                                description = '''
                                    Gather and analyze the latest news and
                                    market sentiment surrounding
                                    {company}'s stock. Provide a summary
                                    of the news and any notable shifts in sentiment.
                                ''',
                                agent = researcher,
                                expected_output = '''
                                    Your final answer MUST be a detailed
                                    summary of the news and market
                                    sentiment surrounding the stock.
                                ''',
                            )
technical_analysis          = Task(
                                description = '''
                                    Conduct a technical analysis of the {company}
                                    stock price movements and identify
                                    key support and resistance levels chart patterns.
                                ''',
                                agent = technical_analyst,
                                expected_output = '''
                                    Your final answer MUST be a report
                                    with potential entry points, price targets
                                    and any other relevant information.
                                ''',
                            )
financial_analysis          = Task(
                                description = '''
                                    Analyze teh {company}'s financial statements,
                                    balance sheet, insider trading data
                                    and other metrics to evaluate {company}'s
                                    financial health and performance.
                                ''',
                                agent = financial_analyst,
                                expected_output = '''
                                    Your final answer MUST be a report with
                                    an overview of {company}'s
                                    revenue, earnings, cash flow, and
                                    other key financial metrics.
                                ''',
                            )
investment_recommendation   = Task(
                                description = '''
                                    Based on the research, technical anaysis, and
                                    financial analysis reports, provide a detailed
                                    investment recommendation for {company} stock.
                                ''',
                                agent = hedge_fund_manager,
                                expected_output = '''
                                    Your final answer MUST be a detailed
                                    recommandation to BUY, SELL or HOLD the stock.
                                    Provide a clear rationable for your recommendation.
                                ''',
                                context = [
                                    research,
                                    technical_analysis,
                                    financial_analysis,
                                ],
                                output_file = 'investment_recommendation.md'
                            )