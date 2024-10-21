import csv
from typing import Tuple, List, Dict, Any


def analyze_employee_data(
    filepath: str,
) -> Tuple[int, Dict[str, int], str, List[Tuple[float, str]]]:
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        employees = list(reader)

    total_employees = len(employees)

    gender_count = {"Male": 0, "Female": 0}
    job_level_count = {}
    highest_problem_solving = {
        "Male": (0.0, "Male"),
        "Female": (0.0, "Female"),
    }

    for employee in employees:
        gender = employee["Gender"]
        job_level = employee["JobLevel"]
        problem_solving_score = round(
            float(employee["ProblemSolvingScore"]), 2
        )

        gender_count[gender] += 1

        if job_level in job_level_count:
            job_level_count[job_level] += 1
        else:
            job_level_count[job_level] = 1

        if problem_solving_score > highest_problem_solving[gender][0]:
            highest_problem_solving[gender] = (problem_solving_score, gender)

    most_common_job_level = sorted(
        job_level_count.items(), key=lambda x: (-x[1], x[0])
    )[0][0]

    highest_scores = sorted(
        [highest_problem_solving["Female"], highest_problem_solving["Male"]],
        key=lambda x: (-x[0], x[1]),
    )

    return total_employees, gender_count, most_common_job_level, highest_scores


def analyze_sales_data(
    filepath: str,
) -> Tuple[Dict[str, int], Dict[str, float], float, List[str]]:
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        sales_data = list(reader)

    product_sales = {}
    region_sales = {}
    product_ids_with_max_sale = []
    highest_sale_amount = 0.0
    region_sales_count = {}

    for sale in sales_data:
        product_category = sale["ProductCategory"]
        sales_region = sale["SalesRegion"]
        sale_amount = float(sale["SaleAmount"])
        product_id = sale["ProductID"]

        if product_category in product_sales:
            product_sales[product_category] += 1
        else:
            product_sales[product_category] = 1

        if sales_region in region_sales:
            region_sales[sales_region] += sale_amount
            region_sales_count[sales_region] += 1
        else:
            region_sales[sales_region] = sale_amount
            region_sales_count[sales_region] = 1

        if sale_amount > highest_sale_amount:
            highest_sale_amount = sale_amount
            product_ids_with_max_sale = [product_id]
        elif sale_amount == highest_sale_amount:
            product_ids_with_max_sale.append(product_id)

    for region in region_sales:
        region_sales[region] = round(
            region_sales[region] / region_sales_count[region], 2
        )

    return (
        product_sales,
        region_sales,
        round(highest_sale_amount, 2),
        product_ids_with_max_sale,
    )


def analyze_bank_data(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        transactions = list(reader)

    deposit_descriptions = set()
    withdrawal_descriptions = set()

    for transaction in transactions:
        description = transaction["TransactionDescription"]
        if transaction["TransactionType"] == "Deposit":
            deposit_descriptions.add(description)
        else:
            withdrawal_descriptions.add(description)

    only_deposit = sorted(deposit_descriptions - withdrawal_descriptions)
    only_withdrawal = sorted(withdrawal_descriptions - deposit_descriptions)
    common_descriptions = sorted(
        deposit_descriptions & withdrawal_descriptions
    )
    exclusive_count = len(only_deposit) + len(only_withdrawal)

    return {
        "only_deposit": only_deposit,
        "common": common_descriptions,
        "only_withdrawal": only_withdrawal,
        "exclusive_count": exclusive_count,
    }
