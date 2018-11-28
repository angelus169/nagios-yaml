{
    'version': {
        'required': True,
        'type': 'string'
    },
    'objects': {
        'required': True,
        'type': 'dict',
        'schema': {
            'hosts': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'hostgroups': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'services': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'servicegroups': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'contacts': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'contactgroups': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'timeperiods': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'commands': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'servicedependencies': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'serviceescalations': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'hostdependencies': {
                'required': True,
                'type': 'dict',
                'schema': {}
            },
            'hostescalations': {
                'required': True,
                'type': 'dict',
                'schema': {}
            }
        }
    }
}
