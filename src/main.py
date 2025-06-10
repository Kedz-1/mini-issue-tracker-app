from fastapi import FastAPI, HTTPException
from src.models import Issue
from typing import List
from uuid import uuid4

app = FastAPI()
issues = {}

@app.post("/issues", response_model = Issue)
async def create_issue(issue:Issue):

    '''

    Creates a ticket for a customer's issue using the 'Issue' base model. Automatically assigns a UUID as the ID.

    Args:
        issue (Issue) - The ticket data, including a title, description, and an optional status (defaults to "Open").

    Returns:
        The newly created ticket including the generated UUID.

    Example Request Body:
    {
        "title": "Example bug",
        "description": "This is a test bug",
        "status": "Open"
    }

    Example Response:
    {
        "id": "a6f0f11b-6820-4ca5-b7bb-ec3874f0dd1f",
        "title": "Example bug",
        "description": "This is a test bug",
        "status": "Open"
    }

    '''
    # Creates a random id and saves it as a string to a variable named issue_id, then appends the value into a the id key in issues, and finally pushes the ticket into the id as a key - value pair.
    issue_id = str(uuid4()) 
    issue.id = issue_id
    issues[issue_id] = issue
    
    # Returns the issue
    return issue


@app.get('/issues', response_model= List[Issue])
async def get_issues():

    '''
    Retrieves a list of all submitted tickets. 

    Returns:
        List[Issue] - A list of all issues stored in the in-memory dictionary.
    


    Examples:
    GET http://127.0.0.1:8000/issues


    Example Response: 
    [
        {
            "id": "a6f0f11b-6820-4ca5-b7bb-ec3874f0dd1f",
            "title": "This is an example bug ",
            "description": "This is a test bug",
            "status": "Open"
        },
        {
            "id": "f48c7aa4-ac96-498c-84ec-0029befb4103",
            "title": "This is an example bug number 2",
            "description": "This is another test bug",
            "status": "Open"
        },
    ...
    ]
    '''

    # return statement for the values and puts them into a list
    return list(issues.values())

@app.get('/issues/{issue_id}', response_model = Issue)
async def get_issue_by_id(issue_id: str):
    
    '''
    Retrieves a specific ticket by its unique ID.

    Args:
        issue_id (str) - The UUID of the issue to retrieve.

    Returns:
        Issue - The issue that matches the given ID.
    
    Raises:
        HTTPException - If the issue ID is not found.

    Example Issues:
    [
        {
            "id": "a6f0f11b-6820-4ca5-b7bb-ec3874f0dd1f",
            "title": "This is an example bug ",
            "description": "This is a test bug",
            "status": "Open"
        },
        {
            "id": "f48c7aa4-ac96-498c-84ec-0029befb4103",
            "title": "This is an example bug number 2",
            "description": "This is another test bug",
            "status": "Open"
        }
    ]

    Example Input: GET http://127.0.0.1:8000/issues/a6f0f11b-6820-4ca5-b7bb-ec3874f0dd1f


    Example Response:
    {
        "id": "a6f0f11b-6820-4ca5-b7bb-ec3874f0dd1f",
        "title": "This is an example bug ",
        "description": "This is a test bug",
        "status": "Open"
    }

    '''

    # Conditional statement where if the issue_id is not found a HTTP Exception is raised with a message mentioning this.
    if issue_id not in issues:
        raise HTTPException(
            status_code = 404,
            detail = 'Issue not found.'
        )
    # Returns the specified issue that matches the id 
    else:
        return issues[issue_id]


@app.delete('/issues/{issue_id}')
async def delete_issue(issue_id):

    if issue_id not in issues:
        raise HTTPException(
            status_code=404,
            detail= 'Issue not found'
        )
    
    else:
        del issues[issue_id]
        return{
            'message': f'Ticket has been deleted: {issue_id}'
        }



