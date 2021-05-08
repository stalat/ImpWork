"""
Role Based Access Control:

Implement a role based auth system. System should be able to assign a role to user and remove a user from the role.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level(Ex: READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role.One user can have multiple roles. Given a user, action type and resource system should be able to tell whether user has access or not.
"""


user_list = dict()
role_list = dict()

class User(object):
    """
    This will create a user and returns a User object whenever needed
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self):
        # creates a user with given first-name & last-name
        print("New user is created with username as: {0}{1}".format(self.first_name, self.last_name))
        user_list.update({self.first_name + self.last_name: {'first_name': self.first_name, 'last_name': self.last_name, 'assigned_roles': []}})

    def get_user(self, username=None):
        # function to return list of users
        if username:
            expected_user = user_list.get(username)
            if not expected_user:
                print("No such user exists with this username")
                return False
            return expected_user
        return user_list

# The user_list would have been modified to
# [{'TalatParwez': {'first_name': 'Talat', 'last_name': 'Parwez'}}, {'MohanBhargava': {'first_name': 'Mohan', 'last_name': 'Bhargava'}}]

class  Role(object):
    """
    Role based authentication system, System should be able to assign a role to a user
    Remove a user from the role
    Entities:
    User, Action Type, Resource, Role
        1. User --> User
        2. ActionType --> Read/Write/Delete
        3. Role  --> Whatever role is given to User
        4. Resource --> The resource, the user will try to access
        ActionType defines the access level (READ/WRITE/DELETE)
        Access to resources for users are controlled by the role, One user can have multiple roles
        Given a user, ActionType and Resource system should be able to tell whether user has access or not
    """
    # a class to define roles and assign roles to action type to various resources,
    # considering, we have 3 resources:
    # 1. chat_messages (READ)
    # 2. blog_content (WRITE)
    # 3. post_comments (DELETE)
    def __init__(self):
        # assigning action type to Resources that a role can perform over resources
        resource_dict = dict()
        resource_dict["READ"] = ['chat_messages', 'post_comments']
        resource_dict["WRITE"] = ['blog_content']
        resource_dict["DELETE"] = ['post_comments']

        for idx, resource in enumerate(resource_dict.items()):
            # this will simply create a role by appending into role_list
            role_list.update({'role_'+str(idx): {'action_type': resource[0], 'resource': resource[1]}})

    @staticmethod
    def user_role_validation(username, role):
        user_data = user_list.get(username)
        if not user_data:
            print("There does not exist such user with username as: {0}".format(username))
            return False
        if role not in role_list:
            print("There does not exist such Role with name: {0}, hence cannot be assigned to User".format(role))
            return False
        return True
        
    def assigning_role_to_user(self, username, role):
        # The role will be assigned to user and gets updated to User records which will tell what all Roles have
        # been assigned to this user
        is_user_valid = self.user_role_validation(username, role)
        user_data = user_list.get(username)

        if not is_user_valid:
            return
        
        # Assign this role to user and let end-user know the available roles to given user
        user_data.get('assigned_roles').append(role)

        # provide the information about that User has been assigned to given role
        print("USER {0} has been assigned to ROLE: {1} and here's a complete list of ROLES to which user is assigned: {2}".format(\
            username, role, user_list.get(username).get('assigned_roles')))
        return

    def removing_user_from_role(self, username, role):
        # checking if the given user & roles are valid from our records
        is_user_valid = self.user_role_validation(username, role)
        if not is_user_valid:
            return
        
        user_data = user_list.get(username)
        # removing the assigned role from given user
        user_data.get('assigned_roles').remove(role)

        print("USER: {0} has been removed from the ROLE: {1}".format(username, role))

    def check_user_access(self, username, action_type, resource):
        # function to check if User has access to resource with action type (READ/WRITE/DELETE)
        user = user_list.get(username)
        access_flag = False

        # get the list of ROLES that this user is been assigned to
        user_data = user_list.get(username)
        assigned_roles = user_data.get('assigned_roles')

        # check what all the actions can user perform over resource
        for role in assigned_roles:
            role_object = role_list.get(role)
            # check which resource he wants to access
            if resource in role_object.get('resource') and action_type in role_object.get('action_type'):
                print("User can access this resource")
                return
                
        print("User cannot access this resource")
