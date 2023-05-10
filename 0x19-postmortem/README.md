### Postmortem
![img_3378](https://github.com/Cathyrt/alx-system_engineering-devops/assets/110995939/cd3ea530-53b2-4c26-a581-21a18aeca6cd)

## Summary

The web server experienced a 100% outage due to Nginx not listening on all active IPs on port 8080, and the firewall was blocking incoming traffic. The issue was resolved by updating the configuration and firewall rules. To prevent similar issues, regular maintenance checks, monitoring systems, and backups were implemented.
