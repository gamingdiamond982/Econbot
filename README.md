# Econbot
This is the repo for the Economy Bot in [r/SimDemocracy](https://www.reddit.com/r/SimDemocracy).

## Backend Types
| Argument Name | Type |
| --- | --- |
| **name** | String |
| **id** | String (on reddit) / Integer (on discord) |
| **server** | String (on reddit) / Integer (on discord) |
| **sender_id** | String (on reddit) / Integer (on discord) |
| **receiver_id** | String (on reddit) / Integer (on discord) |
| **reddit_id** | String (on reddit) / None (anywhere else) |
| **discord_id** | Integer (on discord) / None (anywhere else) |
| **amount** | Integer |
| **time** | Integer |
| **citizen** | Boolean |
| **currency_name** | String |
| **lock_level** | Integer |
| **forced** | Boolean |
| **path** | String |

## Calls to the backend

| Function Call | Return Type | Use | Backend only? |
| --- | --- | --- | --- |
| **databaseCheck()** |  | Checks the integrity of the database structure and will try to fix it. | No |
| **add_account(name, id, server, citizen)** |  | Adds an account to a SimNation database. If citizen is set to true, the user is considered a citizen on that server. | No |
| **add_server(name, reddit_id, discord_id, currency_name)** |  | Will add a server database and make a entry in the master table. | No |
| **money_transfer(sender_id, receiver_id, amount, server, forced)** |  | Transfers money from one user to another user in the **same** server. | No |
| **print_money(server, amount)** | | Schedules a completion date for money to finish being printed. | No |
| **check_print(server)** | | Checks if the server already completed printing money, should a completion date be scheduled. | Yes |
| **get_govt_balance(server)** | Integer | Gets the current amount of money a certain government account holds. Will also run check_print() on the server. | No |
| **get_account_balance(id, server)** | Integer | Gets the current amount of money a certain user account holds. | No |
| **auth_level(id, server)** | Integer | Gets the authorization level of the user in that server. Returns 0 if they don't have any special authorization, 1 if they are an admin and 2 if it's a developer. | No |
| **add_local_admin(id, server)** | | Adds a local admin to a server. | No |
| **add_lock(id, server, lock_level, time)** | | Locks an account for a set amount of time. | No |
| **lock_level(id, server)** | Integer | Gets how an account is locked (if it is at all). 0 is unlocked, 1 is frozen (by government), and 2 is locked by the user. It is encouraged to use is_locked though. | No |
| **is_locked(id, server)** | Boolean | Checks if an user account was locked. | No |
| **list_servers()** | Tuple | Lists all existing servers. | No |
| **list_accounts(server)** | Tuple | Lists all existing accounts in a server. | No |
| **uncheck_get_govt_balance(server)** | Integer | Gets the current amount of money a certain government account holds. Will not run check_print() on the server. | Yes |
| **server_name_by_id(server)** | String | Gets the servers name by the servers ID. (Not useful, because the frontend already knows the name!) | Yes |
| **currency_name(server)** | String | Tells you the currency name of the money on one particular server. | No |
| **id_to_uuid(id)** | String | Gets the internal UUID from the user ID of discord or reddit. | Yes |
| **get_id_type(id)** | String | Tells you the type of a given user or server ID. | Yes |
| **name_exists(name)** | Boolean | Checks the auth table for the given name. | No |
| **account_exists(name, server)** | Boolean | Checks if a user with a certain name has an account in a specific server. | No |
| **id_exists(id, server)** | Boolean | Checks if a user with a certain id has an account in a specific server. | No |
| **\_open_db(path)** | sqlite3.database | Opens a database. **DO NOT USE** | Yes |
