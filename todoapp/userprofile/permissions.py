from rest_framework.permissions import BasePermission


class UserIsOwnerTodo(BasePermission):

    def has_object_permission(self, request, view, freelancer):
        return request.user.id == freelancer.user.id
