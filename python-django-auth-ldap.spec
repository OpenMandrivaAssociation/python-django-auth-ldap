%define modname django-auth-ldap
%define name    python-%{modname}
%define version 1.0.5
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Django LDAP authentication backend
License:	BSD
Group: 		Development/Python
Url: 		http://pypi.python.org/pypi/django-auth-ldap/
Source0: 	http://pypi.python.org/packages/source/d/django-auth-ldap/django-auth-ldap-%{version}.tar.gz
BuildRequires:	    python
Requires:	    python-django
Requires:	    python-ldap
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.

%prep
%setup -q -n %modname-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{python_sitelib}/django_auth_ldap
%{python_sitelib}/django_auth_ldap-%{version}-py%{pyver}.egg-info
