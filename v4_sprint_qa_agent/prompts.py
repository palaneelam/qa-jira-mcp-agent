def scenario_prompt(jira_issue):
    return f"""
You are a Senior QA Engineer.

Generate test scenarios from the Jira story.

Return ONLY valid JSON in this format:

{{
  "scenarios": [
    {{
      "Scenario_ID": "TS001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Scenario_Type": "Positive",
      "Scenario": "Verify successful payment using valid card details"
    }}
  ]
}}

Jira Issue:
{jira_issue}
"""


def test_case_prompt(jira_issue):
    return f"""
You are a Senior QA Engineer.

Generate detailed manual test cases from the Jira story.

Return ONLY valid JSON in this format:

{{
  "test_cases": [
    {{
      "TC_ID": "TC001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Scenario": "Successful payment using valid card details",
      "Precondition": "User has items in cart and valid card details",
      "Steps": "1. Open checkout page\\n2. Enter valid card details\\n3. Submit payment",
      "Expected_Result": "Payment should be successful and order should be confirmed",
      "Priority": "High"
    }}
  ]
}}

Jira Issue:
{jira_issue}
"""


def rtm_prompt(jira_issue):
    return f"""
You are a QA Lead.

Create Requirement Traceability Matrix from the Jira story.

Return ONLY valid JSON in this format:

{{
  "rtm": [
    {{
      "Requirement_ID": "REQ001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Requirement": "User should be able to pay using valid card",
      "Test_Scenario_ID": "TS001",
      "Test_Case_ID": "TC001",
      "Coverage_Status": "Covered"
    }}
  ]
}}

Jira Issue:
{jira_issue}
"""


def risk_prompt(jira_issue):
    return f"""
You are a QA Lead.

Identify QA risks from the Jira story.

Return ONLY valid JSON in this format:

{{
  "risks": [
    {{
      "Risk_ID": "R001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Risk_Type": "Business Risk",
      "Risk_Description": "Customer may be charged twice",
      "Impact": "High",
      "Mitigation": "Test duplicate transaction prevention"
    }}
  ]
}}

Jira Issue:
{jira_issue}
"""


def test_data_prompt(jira_issue):
    return f"""
You are a QA Test Data Specialist.

Generate test data from the Jira story.

Return ONLY valid JSON in this format:

{{
  "test_data": [
    {{
      "Data_ID": "TD001",
      "Issue_Key": "{jira_issue.get("issue_key", "")}",
      "Data_Type": "Valid",
      "Field": "Card Number",
      "Value": "4111111111111111",
      "Purpose": "Valid Visa card payment"
    }}
  ]
}}

Jira Issue:
{jira_issue}
"""

def cross_story_risk_prompt(jira_issues):
    return f"""
  You are a QA Test Manager.

  Analyze the Jira stories below and identify sprint-level cross-story risks.

  Return ONLY valid JSON in this format:

  {{
    "cross_story_risks": [
      {{
        "Risk_ID": "CSR001",
        "Risk_Type": "Integration Risk",
        "Related_Issues": "SCRUM-8, SCRUM-9",
        "Risk_Description": "Coupon discount calculation may impact payment amount validation",
        "Impact": "High",
        "Mitigation": "Perform end-to-end checkout testing covering coupon and payment flow"
      }}
    ]
  }}

  Jira Stories:
  {jira_issues}
  """


def sprint_summary_prompt(jira_issues):
    return f"""
  You are a Senior QA Manager.

  Create a sprint-level QA readiness summary from the Jira stories below.

  Return ONLY valid JSON in this format:

  {{
    "sprint_summary": [
      {{
        "Area": "Scope",
        "Summary": "Payment, coupon, and order confirmation stories are included",
        "QA_Recommendation": "Perform end-to-end checkout validation"
      }}
    ]
  }}

  Jira Stories:
  {jira_issues}
  """

def complete_qa_artifacts_prompt(jira_issue):
    return f"""
    You are a Senior QA Engineer.

    Generate complete QA artifacts from the Jira story.

    Return ONLY valid JSON in this format:

    {{
      "scenarios": [
        {{
          "Scenario_ID": "TS001",
          "Issue_Key": "{jira_issue.get("issue_key", "")}",
          "Scenario_Type": "Positive",
          "Scenario": "Verify successful payment"
        }}
      ],
      "test_cases": [
        {{
          "TC_ID": "TC001",
          "Issue_Key": "{jira_issue.get("issue_key", "")}",
          "Scenario": "Successful payment",
          "Precondition": "User has valid card and items in cart",
          "Steps": "1. Open checkout page\\n2. Enter valid card details\\n3. Submit payment",
          "Expected_Result": "Payment should be successful",
          "Priority": "High"
        }}
      ],
      "rtm": [
        {{
          "Requirement_ID": "REQ001",
          "Issue_Key": "{jira_issue.get("issue_key", "")}",
          "Requirement": "User should be able to make payment",
          "Test_Scenario_ID": "TS001",
          "Test_Case_ID": "TC001",
          "Coverage_Status": "Covered"
        }}
      ],
      "risks": [
        {{
          "Risk_ID": "R001",
          "Issue_Key": "{jira_issue.get("issue_key", "")}",
          "Risk_Type": "Business Risk",
          "Risk_Description": "Duplicate payment may occur",
          "Impact": "High",
          "Mitigation": "Test duplicate transaction prevention"
        }}
      ],
      "test_data": [
        {{
          "Data_ID": "TD001",
          "Issue_Key": "{jira_issue.get("issue_key", "")}",
          "Data_Type": "Valid",
          "Field": "Card Number",
          "Value": "4111111111111111",
          "Purpose": "Valid card payment"
        }}
      ]
    }}

    Jira Issue:
    {jira_issue}
    """