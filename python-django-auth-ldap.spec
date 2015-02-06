%define debug_package %{nil}
%define modname django-auth-ldap

Name: 		python-%{modname}
Version: 	1.2.0
Release: 	2
Summary: 	Django LDAP authentication backend
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/django-auth-ldap/
Source0: 	https://pypi.python.org/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz
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
