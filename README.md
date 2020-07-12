# 🌳 treesaver

Restore any GitHub tree after you **accidentally force push**.

### How to use it

1. Clone this repo and `cd` to it.
2. Find the `SHA` string of the tree you'd like to restore by accessing
`https://api.github.com/repos/<your_username_or_org>/<repo>/events`.
3. In the `payload` property corresponding to your push event, find the `commit` you'd like to revert to and click on its `url`.
4. Under `commit.tree`, copy the `tree`'s `url`.
5. Run `python3 main.py <tree_url> <path_to_save_to>`.

> Example: `python3 main.py https://api.github.com/repos/<username>/<repo>/git/trees/<tree_sha> .`

### Author

Anthony Krivonos ([Portfolio](https://anthonykrivonos.com) | [Github](https://github.com/anthonykrivonos))