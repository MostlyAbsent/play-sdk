# Challenge Background

<!-- TODO: Reference the article. Explain the issue. -->

<!-- TODO: Add references or requirement for POST and JSON data on the wire -->

<!-- TODO: Should I explain the unpack operator is the problem? I think that would be too easy. -->

# Example Payloads 

## Testing Intended Input

Testing the endpoint with the following POST content.

``` json
{
    "firstName" : "Robert"
}
```

### Expected Output

``` json
[
    {
        "firstName": "Robert",
        "lastName": "Smith"
    }
]
```

## Testing Malicious Input

``` json
{
    "manager__user__password__startswith": "p"
}
```

### Expected Output

``` json
[
    {
        "firstName": "Alice",
        "lastName": "Smith"
    }
]
```

Why?

Internally Django, by default stores a password hash that may look like this: `pbkdf2_sha256$26000...`

The query we provided `manager__user__password__startswith` allows us to match, one character at a time, the stored password hash for the manager for this employee. As long as Alice remains in our response set, we know our password guess was correct.[^1]

# Challenge

Mitigate this vulnerability.

# Footnotes

[^1]: This sensitive data can be stored by an attacked for offline cracking. The vulnerability exposed herein can be exploited by similar payloads to reveal unencrypted data if it is within the database. See the full article for a more in-depth overview of the extent of the vulnerability.
