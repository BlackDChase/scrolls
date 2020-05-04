# scrolls

## How to use

```bash
# Install yarn package manager
# Source: https://stackoverflow.com/questions/42606941/install-yarn-ubuntu-16-04-linux-mint-18-1
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn

# Install the required packages using the package manager
yarn install

# Start the web app server
yarn start
```
