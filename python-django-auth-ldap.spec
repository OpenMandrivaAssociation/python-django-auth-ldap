%define _debugsource_template %{nil}
%define module django-auth-ldap
%define oname django_auth_ldap

Name: 		python-django-auth-ldap
Version:	5.3.0
Release:	1
Summary: 	Django LDAP authentication backend
License:	BSD-2-Clause
Group: 		Development/Python
URL: 		https://github.com/django-auth-ldap/django-auth-ldap
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(django)
BuildRequires:	python%{pyver}dist(python-ldap)

%description
This is a Django authentication backend that authenticates
against an LDAP service.

Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for
working with users, groups and permissions.

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.rst
%license LICENSE
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}.dist-info
