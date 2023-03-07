from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    message = 'Редактирование записей разрешено только автору.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

    def has_permission(self, request, view):
        if request.method == 'POST' and not request.user.is_authenticated:
            return False
        if request.method == 'GET' and not request.user.is_authenticated:
            return False
        return True


class IsCommentAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
