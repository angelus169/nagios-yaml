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
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'hostgroups': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'services': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'servicegroups': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'contacts': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'contactgroups': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'timeperiods': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'commands': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'servicedependencies': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'serviceescalations': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'hostdependencies': {
                'required': False,
                'type': 'dict',
                'schema': {}
            },
            'hostescalations': {
                'required': False,
                'type': 'dict',
                'schema': {}
            }
        }
    }
}
