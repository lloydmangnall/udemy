# shelve does have some drawbacks:
    # pickling does add overhead
    # opens the possibility to introduce data from untrusted sources
    # does not support concurrency
import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:  # 'writeback' option enable updating of data via option 1 below
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # option 1: enable 'writeback' option on the shelve database (doesn't write until the shelve is closed or synced)
    # recipes["scrambled eggs"].append("ham")  # will not update the shelve data unless 'writeback' option enabled above
    # recipes["soup"].append("croutons")

    # option 2: update in memory and then the entire immutable shelve object
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # option 3: using the .sync method (be careful as .sync clears the cache)
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])