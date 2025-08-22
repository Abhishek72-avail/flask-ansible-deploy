#!/bin/bash

echo "🚀 Flask + PostgreSQL + Nginx Stack"
echo "=================================="
echo ""
echo "✅ Application is running at: http://localhost"
echo ""
echo "📋 Available endpoints:"
echo "   • Main page:      http://localhost/"
echo "   • Health check:   http://localhost/health"
echo "   • Database test:  http://localhost/db"
echo "   • System status:  http://localhost/api/status"
echo ""
echo "🔧 Services status:"
echo -n "   • Flask app:      "
sudo systemctl is-active flaskapp
echo -n "   • Nginx:          "
sudo systemctl is-active nginx
echo -n "   • PostgreSQL:     "
sudo systemctl is-active postgresql
echo ""

# Try to open in browser (works on systems with GUI)
if command -v xdg-open > /dev/null; then
    echo "🌐 Opening application in browser..."
    xdg-open http://localhost
elif command -v open > /dev/null; then
    echo "🌐 Opening application in browser..."
    open http://localhost
else
    echo "💡 Open http://localhost in your web browser to see the application"
fi
