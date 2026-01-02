import genesis as gs
import IPython

gs.init(backend=gs.gpu, precision="32", logging_level="warning", performance_mode=True)
dt = 0.02

scene = gs.Scene(
    sim_options=gs.options.SimOptions(
        dt=dt,
        substeps=2,
    ),
    rigid_options=gs.options.RigidOptions(
        enable_self_collision=False,
        tolerance=1e-5,
        # For this locomotion policy, there are usually no more than 20 collision pairs. Setting a low value
        # can save memory. Violating this condition will raise an exception.
        max_collision_pairs=20,
    ),
    viewer_options=gs.options.ViewerOptions(
        camera_pos=(2.0, 0.0, 2.5),
        camera_lookat=(0.0, 0.0, 0.5),
        camera_fov=40,
        max_FPS=int(1.0 / dt),
    ),
    vis_options=gs.options.VisOptions(rendered_envs_idx=[0]),
    show_viewer=True,
)

# add plain
scene.add_entity(
    gs.morphs.URDF(
        file="urdf/plane/plane.urdf",
        fixed=True,
    )
)

# add robot
robot = scene.add_entity(
    gs.morphs.URDF(
        file="unitree_ros/robots/g1_description/g1_23dof.urdf",
        pos=[0.0, 0.0, 0.8],
        quat=[1.0, 0.0, 0.0, 0.0],
    ),
)

scene.build(n_envs=1)

IPython.embed()

'''
Links
0 pelvis [0.  0.  0.8]
1 left_hip_pitch_link [ 0.        0.064452 -0.1027  ]
2 right_hip_pitch_link [ 0.       -0.064452 -0.1027  ]
3 torso_link [-0.0039635  0.         0.054    ]
4 left_hip_roll_link [ 0.        0.052    -0.030465]
5 right_hip_roll_link [ 0.       -0.052    -0.030465]
6 left_shoulder_pitch_link [0.0039563 0.10022   0.23778  ]
7 right_shoulder_pitch_link [ 0.0039563 -0.10021    0.23778  ]
8 left_hip_yaw_link [ 0.025001  0.       -0.12412 ]
9 right_hip_yaw_link [ 0.025001  0.       -0.12412 ]
10 left_shoulder_roll_link [ 0.        0.038    -0.013831]
11 right_shoulder_roll_link [ 0.       -0.038    -0.013831]
12 left_knee_link [-0.078273   0.0021489 -0.17734  ]
13 right_knee_link [-0.078273  -0.0021489 -0.17734  ]
14 left_shoulder_yaw_link [ 0.       0.00624 -0.1032 ]
15 right_shoulder_yaw_link [ 0.      -0.00624 -0.1032 ]
16 left_ankle_pitch_link [ 0.0000e+00 -9.4445e-05 -3.0001e-01]
17 right_ankle_pitch_link [ 0.0000e+00  9.4445e-05 -3.0001e-01]
18 left_elbow_link [ 0.015783  0.       -0.080518]
19 right_elbow_link [ 0.015783  0.       -0.080518]
20 left_ankle_roll_link [ 0.        0.       -0.017558]
21 right_ankle_roll_link [ 0.        0.       -0.017558]
22 left_wrist_roll_rubber_hand [ 0.1         0.00188791 -0.01      ]
23 right_wrist_roll_rubber_hand [ 0.1        -0.00188791 -0.01      ]
'''

'''
Joints
0 root_joint
1 left_hip_pitch_joint
2 right_hip_pitch_joint
3 waist_yaw_joint
4 left_hip_roll_joint
5 right_hip_roll_joint
6 left_shoulder_pitch_joint
7 right_shoulder_pitch_joint
8 left_hip_yaw_joint
9 right_hip_yaw_joint
10 left_shoulder_roll_joint
11 right_shoulder_roll_joint
12 left_knee_joint
13 right_knee_joint
14 left_shoulder_yaw_joint
15 right_shoulder_yaw_joint
16 left_ankle_pitch_joint
17 right_ankle_pitch_joint
18 left_elbow_joint
19 right_elbow_joint
20 left_ankle_roll_joint
21 right_ankle_roll_joint
22 left_wrist_roll_joint
23 right_wrist_roll_joint
'''