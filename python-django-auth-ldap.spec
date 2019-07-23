%define debug_package %{nil}
%define modname django-auth-ldap

Name: 		python-%{modname}
Version:	2.0.0
Release:	1
Summary: 	Django LDAP authentication backend
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/django-auth-ldap/
Source0:	https://files.pythonhosted.org/packages/ec/95/1e7f1ee3f9ea654ae3b693662fae5112bd7827e6e1b5222f8bcf1720a2aa/django-auth-ldap-2.0.0.tar.gz
BuildRequires:	    python-devel
BuildRequires:	    python-distribute
Requires:	    python-django
Requires:	    python-ldap

%description
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

%prep
%setup -q -n %modname-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc docs/*
%{py_puresitedir}/django_auth_ldap
%{py_puresitedir}/django_auth_ldap-%{version}-py*.egg-info
