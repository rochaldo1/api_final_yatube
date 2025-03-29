from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user',)

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        if Follow.objects.filter(
            user=self.context['request'].user,
            following=data['following']
        ).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого автора"
            )
        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        read_only_fields = ('author', 'pub_date')

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст не может быть пустым.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('author', 'post', 'created')
