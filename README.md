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

**add_local_admin(id, server)**
Adds a local admin to one server
 
**add_lock(id, server, lock_level, time)**
Id, server is int

Level is int
time is int in seconds

**lock_level(id, server)**
grabs the lock level of a user
0 is unlocked
1 is frozen I think and 2 is locked by user
but you have no reason to run this

**is_locked(id, server)**
both string
amazing

**list_servers()**
only useful for developer commands but you likely wont need to run it

**list_accounts(server)**
maybe useful
but likely not

**uncheck_get_govt_balance(server)**
you wont need this
 
**server_name_by_id(server)**
useless for you because you already know the name

**currency_name(server)**
self explainatory
 
**id_to_uuid(id)**
doubt you'll need this

**get_id_type(id)**
definetly useless, it will always return "discord_id" for you

**name_exists(name)**
checks the auth table if that name is a registered user
returns a boolean

**account_exists(name, server)**
well
obvious
return booleans

**id_exists(id, server)**
obvious too
also a boolean

**open_db(path)**
use this and I will kill you
