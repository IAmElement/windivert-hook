# windivert-hook beta
A study into cracking poorly licensed windows applications using a python based WinDivert hook.

**Example:** 
> Licensed application dubbed "Alpha" needs a username and password to authenticate. In this example, we're going to use a common pay-to-cheat loader.

A user purchases a license to this specific cheat, and therefore they must be issued a unique identifier in order to use the software. This identifier in this case is a username & password. Due to the lack of HTTPS usage, we're able to learn the following through a Wireshark dump:

Upon entering username & password, a GET request is used to establish a WebSocket to home. This socket is simple, and only reponds on four occasions:
```
1. A bad username and password are entered, denying the authentication. 
2. A good username and password are entered, accepting the authentication and proceeding with the cheat injection.
3. The username and password specified are banned, denying the authentication (and probably RATing the user).
4. The username and password specified appear to be connecting from a different computer, denying the authentication.
```

We need to hijack number 2, so we can trick the loader into thinking that auth was okay with our request. We do that by intercepting the TCP traffic returned, and dubbing the payload with our own data. 

This can be adapted to any licensed software which uses some level of backend authentication, and the required responses can be found using Wireshark.
