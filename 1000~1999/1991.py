#https://www.acmicpc.net/problem/1991
#트리 순회

n=int(input())
tree={}
for i in range(n):
    root,left,right=input().split()
    tree[root]=[left,right]

def preorder(tree,root): #전위순회
    if root!='.':
        print(root,end='')
        preorder(tree,tree[root][0]) #왼쪽 자식
        preorder(tree,tree[root][1]) #오른쪽 자식

def inorder(tree,root): #중위순회
    if root!='.':
        inorder(tree,tree[root][0]) #왼쪽 자식
        print(root,end='')
        inorder(tree,tree[root][1]) #오른쪽 자식

def postorder(tree,root): #후위순회
    if root!='.':
        postorder(tree,tree[root][0]) #왼쪽 자식
        postorder(tree,tree[root][1]) #오른쪽 자식
        print(root,end='')

preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')
print()
