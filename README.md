# Flask + Ansible Deployment

This project demonstrates automated deployment of a Flask application with PostgreSQL database and Nginx reverse proxy using Ansible, featuring a beautiful web interface with technology stack visualization.

## 🎨 Features

- **Beautiful Web Interface**: Modern, responsive design with technology stack logos
- **Real-time Status Monitoring**: Live status indicators for all services
- **Technology Stack Showcase**: Visual representation of Flask, PostgreSQL, Nginx, and Gunicorn
- **API Endpoints**: RESTful endpoints for health checks and system status
- **Automated Deployment**: Complete infrastructure as code with Ansible

## 🏗️ Architecture

- **Flask Application**: Python web framework with Jinja2 templates
- **Database**: PostgreSQL 14 with connection monitoring
- **Web Server**: Nginx as reverse proxy server
- **WSGI Server**: Gunicorn for production deployment
- **Process Manager**: systemd services for all components
- **Deployment**: Ansible playbooks for complete automation

## 📁 Components

### Roles

1. **common**: System packages, user creation, basic setup
2. **postgres**: PostgreSQL installation, database and user creation
3. **app**: Flask application deployment, virtual environment, systemd service
4. **nginx**: Nginx configuration and reverse proxy setup

### Frontend Features

- **Technology Cards**: Visual cards showing Flask, PostgreSQL, Nginx, and Gunicorn status
- **Real-time Monitoring**: JavaScript-powered status updates every 30 seconds
- **System Information**: Detailed system and application information
- **API Documentation**: Built-in endpoint documentation
- **Responsive Design**: Mobile-friendly interface with CSS animations

### Configuration

- Application runs on port 8000 (internal)
- Nginx serves on port 80 (external)
- PostgreSQL on default port 5432
- Application user: `flaskapp`
- Application directory: `/opt/flaskapp`

## 🚀 Deployment

Run the playbook:

```bash
ansible-playbook -i inventory.ini site.yml --ask-become-pass
```

## 🌐 Quick Start

After deployment, use the convenience script:

```bash
./open_app.sh
```

Or manually open: http://localhost

## 🔍 Testing

The application provides these endpoints:

### Web Interface
- `/` - Beautiful main application page with stack visualization

### API Endpoints
- `/health` - Health check endpoint (JSON response)
- `/db` - Database connectivity test (JSON response)
- `/api/status` - Complete system status (JSON response)

### Manual Testing

```bash
# Main page (HTML)
curl http://localhost/

# Health check (JSON)
curl http://localhost/health

# Database test (JSON)
curl http://localhost/db

# System status (JSON)
curl http://localhost/api/status
```

## 🔧 Services Management

Check service status:

```bash
# Flask application
sudo systemctl status flaskapp

# Nginx
sudo systemctl status nginx

# PostgreSQL
sudo systemctl status postgresql
```

Restart services:

```bash
# Restart Flask app
sudo systemctl restart flaskapp

# Restart Nginx
sudo systemctl restart nginx

# Restart PostgreSQL
sudo systemctl restart postgresql
```

## 🎯 Frontend Technologies

- **HTML5**: Semantic markup with modern structure
- **CSS3**: Advanced styling with gradients, animations, and responsive design
- **JavaScript**: Real-time status updates and API integration
- **Font Awesome**: Professional icons for technology stack
- **CSS Grid & Flexbox**: Modern layout techniques

## 🛠️ Troubleshooting

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
6. **Frontend Assets**: Added proper static file serving and template structure

### Common Issues

**502 Bad Gateway**: Check if Flask app is running and Nginx configuration is correct
```bash
sudo systemctl status flaskapp
sudo nginx -t
```

**Database Connection Error**: Verify PostgreSQL is running and credentials are correct
```bash
sudo systemctl status postgresql
sudo -u postgres psql -c "\l"
```

**Static Files Not Loading**: Ensure proper file permissions and Nginx configuration
```bash
ls -la /opt/flaskapp/static/
sudo systemctl reload nginx
```

## ⚙️ Variables

Key variables in `group_vars/all.yml`:

- `app_name`: Application name (flaskapp)
- `app_user`: System user for the application
- `app_dir`: Application directory path
- `app_port`: Internal application port (8000)
- `nginx_listen_port`: External nginx port (80)
- `db_name`, `db_user`, `db_password`: Database configuration
- `server_name`: Nginx server name configuration

## 🔒 Security Notes

- Database password is stored in plain text (should use Ansible Vault in production)
- Application runs as dedicated system user
- Nginx acts as reverse proxy (no direct access to Flask app)
- Static files served securely through Nginx
- CSRF protection should be added for production use

## 📊 Monitoring

The application includes built-in monitoring features:

- **Service Status**: Real-time status of all components
- **Database Health**: Connection testing and version information
- **System Metrics**: Timestamp tracking and service availability
- **Error Handling**: Graceful error display and logging

## 🎨 Customization

To customize the frontend:

1. Edit `roles/app/files/templates/index.html` for HTML structure
2. Modify `roles/app/files/static/css/style.css` for styling
3. Update `roles/app/files/app.py` for backend functionality
4. Run the playbook to deploy changes

## 📝 License

This project is open source and available under the MIT License.
