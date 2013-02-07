#!/usr/bin/env python3

"""Demonstrates what 3.3's `yield from` can do for a basic binary tree
implementation.

"""


class BinaryTree:
    def __init__(self, left=None, me=None, right=None):
        self.left = left
        self.me = me
        self.right = right

    def __iter__(self):
        '''Produces an inorder traversal of its items.'''
        if self.left:
            yield from self.left
        if self.me:
            yield self.me
        if self.right:
            yield from self.right


class BinaryTreeOldWay:
    def __init__(self, left=None, me=None, right=None):
        self.left = left
        self.me = me
        self.right = right

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        if self.me:
            yield self.me
        if self.right:
            for node in self.right:
                yield node


