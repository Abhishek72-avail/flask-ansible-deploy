# Flask + Ansible Deployment

This project demonstrates automated deployment of a Flask application with PostgreSQL database and Nginx reverse proxy using Ansible.

## Architecture

- **Flask Application**: Simple web app running on Gunicorn
- **Database**: PostgreSQL 14
- **Web Server**: Nginx as reverse proxy
- **Process Manager**: systemd service for Gunicorn
- **Deployment**: Ansible playbooks for automation

## Components

### Roles

1. **common**: System packages, user creation, basic setup
2. **postgres**: PostgreSQL installation, database and user creation
3. **app**: Flask application deployment, virtual environment, systemd service
4. **nginx**: Nginx configuration and reverse proxy setup

### Configuration

- Application runs on port 8000 (internal)
- Nginx serves on port 80 (external)
- PostgreSQL on default port 5432
- Application user: `flaskapp`
- Application directory: `/opt/flaskapp`

## Deployment

Run the playbook:

```bash
ansible-playbook -i inventory.ini site.yml
```

## Testing

The application provides these endpoints:

- `/` - Main application page
- `/health` - Health check endpoint
- `/db` - Database connectivity test

Test the deployment:

```bash
# Main page
curl http://localhost/

# Health check
curl http://localhost/health

# Database test
curl http://localhost/db
```

## Services

Check service status:

```bash
# Flask application
sudo systemctl status flaskapp

# Nginx
sudo systemctl status nginx

# PostgreSQL
sudo systemctl status postgresql
```

## Troubleshooting

### PostgreSQL Installation Issues

The original issue was with PostgreSQL package installation failing due to apt cache issues. This was resolved by:

1. Properly updating apt cache after clearing stale lists
2. Installing packages in groups to handle dependencies
3. Setting `cache_valid_time: 0` to force cache update
4. Adding explicit `update_cache: no` to subsequent package installations

### Key Fixes Applied

1. **Apt Cache Management**: Fixed cache clearing and updating sequence
2. **Package Installation**: Split into logical groups (basic, nginx, postgresql)
3. **Nginx Configuration**: Added missing `nginx_listen_port` variable
4. **Handler Names**: Fixed case sensitivity in handler names
5. **Site Conflicts**: Removed conflicting nginx sites

## Variables

Key variables in `group_vars/all.yml`:

- `app_name`: Application name (flaskapp)
- `app_user`: System user for the application
- `app_dir`: Application directory path
- `app_port`: Internal application port (8000)
- `nginx_listen_port`: External nginx port (80)
- `db_name`, `db_user`, `db_password`: Database configuration
- `server_name`: Nginx server name configuration

## Security Notes

- Database password is stored in plain text (should use Ansible Vault in production)
- Application runs as dedicated system user
- Nginx acts as reverse proxy (no direct access to Flask app)
