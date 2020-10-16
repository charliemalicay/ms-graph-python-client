from typing import List
from typing import Dict
from typing import Union

from ms_graph.session import GraphSession


class Notes():

    """
    ## Overview:
    ----
    Microsoft Graph lets your app get authorized access to a user's
    OneNote notebooks, sections, and pages in a personal or organization
    account. With the appropriate delegated or application permissions,
    your app can access the OneNote data of the signed-in user or any
    user in a tenant.
    """

    def __init__(self, session: object) -> None:
        """Initializes the `Notes` object.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft Graph Client.
        """

        # Set the session.
        self.graph_session: GraphSession = session

        # Set the endpoint.
        self.endpoint = 'onenote'

    def list_my_notebooks(self) -> Dict:
        """Retrieve a list of your notebook objects.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # define the endpoints.
        endpoint = "me/" + self.endpoint + "/notebooks"

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def list_user_notebooks(self, user_id: str) -> Dict:
        """Retrieve a list of notebook objects.

        ### Parameters
        ----
        user_id (str): The User's ID that is assoicated with
        their Graph account.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "users/{user_id}".format(user_id=user_id) + \
            self.endpoint + "/notebooks"

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def list_group_notebooks(self, group_id: str) -> Dict:
        """Retrieve a list of notebook objects.

        ### Parameters
        ----
        group_id (str): The Group ID that you want to pull
        notebooks for.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "groups/{group_id}".format(
            group_id=group_id) + self.endpoint + "/notebooks"

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def list_site_notebooks(self, site_id: str) -> Dict:
        """Retrieve a list of notebook objects.

        ### Parameters
        ----
        site_id (str): The Site ID that you want to pull
        notebooks for.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "sites/{site_id}".format(site_id=site_id) + \
            self.endpoint + "/notebooks"

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def get_my_notebook(self, notebook_id: str) -> Dict:
        """Retrieve a list of notebook objects.

        ### Parameters
        ----
        notebook_id (str): The User's Notebook ID that you
        want to pull.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # define the endpoints.
        endpoint = "me/" + self.endpoint + "/notebooks/{notebook_id}".format(
            notebook_id=notebook_id
        )

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def get_user_notebook(self, user_id: str, notebook_id: str) -> Dict:
        """Retrieve a notebook object from a user by it's ID.

        ### Parameters
        ----
        user_id (str): The User's ID that is assoicated with
        their Graph account.

        notebook_id (str): The Notebook ID that you
        want to pull.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "users/{user_id}".format(user_id=user_id) + self.endpoint + "/notebooks/{notebook_id}".format(
            notebook_id=notebook_id
        )

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def get_group_notebook(self, group_id: str, notebook_id: str) -> Dict:
        """Retrieve a notebook object from a Group by it's ID.

        ### Parameters
        ----
        group_id (str): The Group ID that you want to pull
        notebooks for.

        notebook_id (str): The Notebook ID that you
        want to pull.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "groups/{group_id}".format(group_id=group_id) + self.endpoint + "/notebooks/{notebook_id}".format(
            notebook_id=notebook_id
        )

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def get_site_notebook(self, site_id: str, notebook_id: str) -> Dict:
        """Retrieve a notebook object from a SharePoint Site by it's ID.

        ### Parameters
        ----
        site_id (str): The Site ID that you want to pull
        notebooks for.

        notebook_id (str): The Notebook ID that you
        want to pull.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = "sites/{site_id}".format(site_id=site_id) + self.endpoint + "/notebooks/{notebook_id}".format(
            notebook_id=notebook_id
        )

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content

    def list_my_notebook_section(self, notebook_id: str) -> Dict:
        """Retrieve a list of onenoteSection objects from one of your notebooks.

        ### Parameters
        ----
        notebook_id (str): The Notebook ID that you
        want to pull.

        ### Returns
        ----
        Dict:
            A List of `Notebook` Resource Object.
        """

        # Define the endpoint.
        endpoint = endpoint = "me/" + self.endpoint + "/notebooks/{notebook_id}".format(
            notebook_id=notebook_id
        ) + "/sections"

        content = self.graph_session.make_request(
            method='get',
            endpoint=endpoint
        )

        return content