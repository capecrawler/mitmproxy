## Mobile Apps API Mock Testing

### Tools
#### mitmproxy
[mitmproxy](https://mitmproxy.org) is an interactive console program that allows traffic flows to be intercepted, inspected, modified and replayed.

##### Installation
Install mitmproxy on your machine using the [docs](http://docs.mitmproxy.org/en/latest/install.html) from the mitmproxy site.
###### macOS
The recommended way to install mitmproxy on macOS is to use [Homebrew](https://brew.sh):

`brew install mitmproxy`

###### Windows
The recommended way to install mitmproxy on Windows is to download the [Self-contained Pre-built Binary Packages](http://docs.mitmproxy.org/en/latest/install.html#binary-packages) from mitmproxy's [releases](https://github.com/mitmproxy/mitmproxy/releases/tag/v2.0.2) page.

After installation, you’ll find shortcuts for [mitmweb](http://docs.mitmproxy.org/en/latest/mitmweb.html#mitmweb) (the web-based interface) and [mitmdump](http://docs.mitmproxy.org/en/latest/mitmdump.html#mitmdump) in the start menu. Both executables are added to your PATH and can be invoked from the command line.

### API Mock Testing
#### Start proxy
Run **mitmproxy** or **mitmweb** to view requests and responses to proxy

- Console:

	`mitmproxy --host`

- Web interface (view in browser):

	`mitmweb --host`

*\*By default, mitmproxy runs on port `8080`*

#### Browser
Setup your browser's proxy to use default mitmproxy port
###### Firefox (recommended)
- Go to `Preferences`, search for `Proxy`, then click `Manual Proxy Configuration`
- Under HTTP Proxy type `127.0.0.1` in the first field, and `8080` under Port.
- Now under SSL Proxy type `127.0.0.1` in the first field, and `8080` under Port. Then hit OK.

###### Chrome
- Go to `Settings`, search for `Proxy`, then click `Open proxy settings`
- This should open up your `Network Preferences`, click on HTTP and set to `127.0.0.1 : 8080`
- Then click on HTTPS and set to `127.0.0.1 : 8080`

###### Download certificate
- Go to http://mitm.it/ to download the certificate and install on your browser

----
## Android
##### Run android emulator and use http-proxy:
- Go to sdk tools

	`cd ~/Library/Android/sdk/tools`

- List all your available AVDs

	`emulator -list-avds`

- Run emulator with http-proxy argument
	`emulator -avd <AVD name> -netdelay none -netspeed full -http-proxy http://<local IP>:8080`
	e.g.
	`emulator -avd Pixel_API_26 -netdelay none -netspeed full -http-proxy http://127.0.0.1:8080`

##### Install mitmproxy certificate to device/emulator
- Go to http://mitm.it/ to download the certificate and install into the device/emulator
OR
- Run mitmweb once to create ssl certificates in `.mitmproxy`
- Copy and install `mitmproxy-ca-cert.cer` from `.mitmproxy` into the device/emulator

##### Update Android app to trust all certificates:
- In the Android project, update the file `TrustAllSSLProtocolSocketFactory.java` in the project `codebase`:

	`private static final boolean TRUST_ALL_SSL_CERTIFICATES = true;`

- This is for **testing** purposes only and **should not be committed**, you should revert this when releasing a build.

##### Run the Android App
- Run the updated Android app and update the JSON responses from `mock` folder for testing.

----

## iOS

#### Make sure that certificate pinning is disabled in the iOS app source code
#### For AFNetworking
- Find the lines instantiating `AFSecurityPolicy` initialize `policyWithPinningMode` to `AFSSLPinningModeNone`
- Make sure `securityPolicy.allowInvalidCertificates` is `NO` (false)

##### iOS Simulator
- Launch iOS Simulator
- Drag and drop the mitm proxy pem file found at `~/.mitmproxy/mitmproxy-ca-cert.pem` to the iOS Simulator
- Set machine's network settings proxy http and https to localhost:8080
- Run `mitmproxy` in your machine
- Run app

##### iOS Device
- Ensure that the machine and phone are connected in the same network
- Update up phone's network proxy manually to `192.168.1.xxx` (machine's IP in the network) with port `8080`
- Run `mitmproxy` in your machine
- Access `http://mitm.it` and choose iOS to install certificate
- Run app

----

## View request / response
Run an API call through your configured browser to view the request / response


- If you are running the **mitmproxy (console)**, you should see the requests and response in your console
- If you are running **mitmweb**, you should see the requests and response in your browser using https://localhost:8081

#### Mock API response
You can mock an API response by using **mitmdump**

- Run the python script in this repository (`scripts/intercept_requests.py`) to mock the `JSON` response
	
	New Version (2.0.2) - `mitmdump -s scripts/intercept_requests.py`
