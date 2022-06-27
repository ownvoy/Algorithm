#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _TreeNode
{
    int data;
    struct _TreeNode *left;
    struct _TreeNode *right;
} TreeNode;

int Llink(TreeNode *Ptreenode, TreeNode *Ctreenode)
{
    Ptreenode->left = Ctreenode;
    return 0;
}

int Rlink(TreeNode *Ptreenode, TreeNode *Ctreenode)
{

    Ptreenode->right = Ctreenode;
    return 0;
}

void inorder(TreeNode *treenode)
{

    if (treenode == NULL)
    {
        return;
    }

    inorder(treenode->left);
    printf("%c", treenode->data);
    inorder(treenode->right);
}

void postorder(TreeNode *treenode)
{

    if (treenode == NULL)
    {
        return;
    }
    postorder(treenode->left);
    postorder(treenode->right);
    printf("%c", treenode->data);
}

void preorder(TreeNode *treenode)
{

    if (treenode == NULL)
    {
        return;
    }
    printf("%c", treenode->data);
    preorder(treenode->left);
    preorder(treenode->right);
}
int main()
{
    int number;
    scanf("%d", &number);

    TreeNode *treenode[number];

    for (int i = 0; i < number; i++)
    {
        treenode[i] = malloc(sizeof(TreeNode));
        treenode[i]->data = i + 65;
        treenode[i]->left = NULL;
        treenode[i]->right = NULL;
    }

    for (int i = 0; i < number; i++)
    {
        char parent;
        char Lchild;
        char Rchild;
        getchar();
        scanf("%c %c %c", &parent, &Lchild, &Rchild);
        int parentNum = (int)parent - 65;
        int LchildNum = (int)Lchild - 65;
        int RchildNum = (int)Rchild - 65;
        // printf("%d %d %d\n", parentNum, LchildNum, RchildNum);
        if (Lchild != '.')
        {
            Llink(treenode[parentNum], treenode[LchildNum]);
        }
        if (Rchild != '.')
        {
            Rlink(treenode[parentNum], treenode[RchildNum]);
        }
    }

    preorder(treenode[0]);
    printf("\n");
    inorder(treenode[0]);
    printf("\n");
    postorder(treenode[0]);

    return 0;
}
