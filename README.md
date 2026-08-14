# rds-password-secret-manager
```text
                         AWS
                          |
            +-------------+-------------+
            |                           |
            ↓                           ↓
           EC2                         RDS
            |                      database-1
            |                           |
       IAM Role                         |
            |                           |
            ↓                           |
     Secrets Manager <------------------+
            |
            | Managed by RDS
            |
            ↓
      Auto-rotated password
            |
            ↓
       Python / Boto3
            |
            ↓
        PyMySQL :3306
            |
            ↓
         RDS MySQL
```


```text
PyMySQL is a Python library/driver that allows Python programs to connect to and communicate with a MySQL database.

In your setup:

Python application
       |
       | PyMySQL
       ↓
    RDS MySQL
Why did we install it?

We installed:

pip3 install pymysql

Then in your Python code:

import pymysql

This gives Python the ability to connect to MySQL.

For example:

connection = pymysql.connect(
    host=RDS_HOST,
    port=3306,
    user=secret["username"],
    password=secret["password"]
)

Here PyMySQL is responsible for the actual MySQL connection.

