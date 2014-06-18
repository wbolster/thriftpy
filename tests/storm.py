# -*- coding: utf-8 -*-

"""
This file shows what dynamically generated
"""

from thriftpy.thrift import (
    TPayload,
    TException,
    TType,
)


class JavaObjectArg(TPayload):
    thrift_spec = {1: (TType.I32, 'int_arg'),
                   2: (TType.I64, 'long_arg'),
                   3: (TType.STRING, 'string_arg'),
                   4: (TType.BOOL, 'bool_arg'),
                   5: (TType.BINARY, 'binary_arg'),
                   6: (TType.DOUBLE, 'double_arg')}


class JavaObject(TPayload):
    thrift_spec = {1: (TType.STRING, 'full_class_name'),
                   2: (TType.LIST, 'args_list', (TType.STRUCT,
                                                 JavaObjectArg))}


class NullStruct(TPayload):
    thrift_spec = {}


class GlobalStreamId(TPayload):
    thrift_spec = {1: (TType.STRING, 'componentId'),
                   2: (TType.STRING, 'streamId')}


class Grouping(TPayload):
    thrift_spec = {1: (TType.LIST, 'fields', TType.STRING),
                   2: (TType.STRUCT, 'shuffle', NullStruct),
                   3: (TType.STRUCT, 'all', NullStruct),
                   4: (TType.STRUCT, 'none', NullStruct),
                   5: (TType.STRUCT, 'direct', NullStruct),
                   6: (TType.STRUCT, 'custom_object', JavaObject),
                   7: (TType.STRING, 'custom_serialized'),
                   8: (TType.STRUCT, 'local_or_shuffle', NullStruct)}


class StreamInfo(TPayload):
    thrift_spec = {1: (TType.LIST, 'output_fields', TType.STRING),
                   2: (2, 'direct')}


class ShellComponent(TPayload):
    thrift_spec = {1: (TType.STRING, 'execution_command'),
                   2: (TType.STRING, 'script')}


class ComponentObject(TPayload):
    thrift_spec = {1: (TType.STRING, 'serialized_java'),
                   2: (TType.STRUCT, 'shell', ShellComponent),
                   3: (TType.STRUCT, 'java_object', JavaObject)}


class ComponentCommon(TPayload):
    thrift_spec = {1: (TType.MAP, 'inputs', ((TType.STRUCT, GlobalStreamId),
                                             (TType.STRUCT, Grouping))),
                   2: (TType.MAP, 'streams', (TType.STRING, (TType.STRUCT,
                                                             StreamInfo))),
                   3: (TType.I32, 'parallelism_hint'),
                   4: (TType.STRING, 'json_conf')}


class SpoutSpec(TPayload):
    thrift_spec = {1: (TType.STRUCT, 'spout_object', ComponentObject),
                   2: (TType.STRUCT, 'common', ComponentCommon)}


class Bolt(TPayload):
    thrift_spec = {1: (TType.STRUCT, 'bolt_object', ComponentObject),
                   2: (TType.STRUCT, 'common', ComponentCommon)}


class StateSpoutSpec(TPayload):
    thrift_spec = {1: (TType.STRUCT, 'state_spout_object', ComponentObject),
                   2: (TType.STRUCT, 'common', ComponentCommon)}


class StormTopology(TPayload):
    thrift_spec = {1: (TType.MAP, 'spouts', (TType.STRING, (TType.STRUCT,
                                                            SpoutSpec))),
                   2: (TType.MAP, 'bolts', (TType.STRING, (TType.STRUCT,
                                                           Bolt))),
                   3: (TType.MAP, 'state_spouts', (TType.STRING,
                                                   (TType.STRUCT,
                                                    StateSpoutSpec)))}


class AlreadyAliveException(TException):
    thrift_spec = {1: (TType.STRING, 'msg')}


class NotAliveException(TException):
    thrift_spec = {1: (TType.STRING, 'msg')}


class InvalidTopologyException(TException):
    thrift_spec = {1: (TType.STRING, 'msg')}


class TopologySummary(TPayload):
    thrift_spec = {1: (TType.STRING, 'id'),
                   2: (TType.STRING, 'name'),
                   3: (TType.I32, 'num_tasks'),
                   4: (TType.I32, 'num_executors'),
                   5: (TType.I32, 'num_workers'),
                   6: (TType.I32, 'uptime_secs'),
                   7: (TType.STRING, 'status')}


class SupervisorSummary(TPayload):
    thrift_spec = {1: (TType.STRING, 'host'),
                   2: (TType.I32, 'uptime_secs'),
                   3: (TType.I32, 'num_workers'),
                   4: (TType.I32, 'num_used_workers'),
                   5: (TType.STRING, 'supervisor_id')}


class ClusterSummary(TPayload):
    thrift_spec = {1: (TType.LIST, 'supervisors', (TType.STRUCT,
                                                   SupervisorSummary)),
                   2: (TType.I32, 'nimbus_uptime_secs'),
                   3: (TType.LIST, 'topologies', (TType.STRUCT,
                                                  TopologySummary))}


class ErrorInfo(TPayload):
    thrift_spec = {1: (TType.STRING, 'error'),
                   2: (TType.I32, 'error_time_secs')}


class BoltStats(TPayload):
    thrift_spec = {1: (TType.MAP, 'acked', (TType.STRING, (TType.MAP,
                                                           ((TType.STRUCT,
                                                             GlobalStreamId),
                                                            TType.I64)))),
                   2: (TType.MAP, 'failed', (TType.STRING, (TType.MAP,
                                                            ((TType.STRUCT,
                                                              GlobalStreamId),
                                                             TType.I64)))),
                   3: (TType.MAP, 'process_ms_avg', (TType.STRING,
                                                     (TType.MAP,
                                                      ((TType.STRUCT,
                                                        GlobalStreamId),
                                                       TType.DOUBLE)))),
                   4: (TType.MAP, 'executed', (TType.STRING,
                                               (TType.MAP, ((TType.STRUCT,
                                                             GlobalStreamId),
                                                            TType.I64)))),
                   5: (TType.MAP, 'execute_ms_avg', (TType.STRING,
                                                     (TType.MAP,
                                                      ((TType.STRUCT,
                                                        GlobalStreamId),
                                                       TType.DOUBLE))))}


class SpoutStats(TPayload):
    thrift_spec = {1: (TType.MAP, 'acked', (TType.STRING, (TType.MAP,
                                                           (TType.STRING,
                                                            TType.I64)))),
                   2: (TType.MAP, 'failed', (TType.STRING, (TType.MAP,
                                                            (TType.STRING,
                                                             TType.I64)))),
                   3: (TType.MAP, 'complete_ms_avg', (TType.STRING,
                                                      (TType.MAP,
                                                       (TType.STRING,
                                                        TType.DOUBLE))))}


class ExecutorSpecificStats(TPayload):
    thrift_spec = {1: (TType.STRUCT, 'bolt', BoltStats),
                   2: (TType.STRUCT, 'spout', SpoutStats)}


class ExecutorStats(TPayload):
    thrift_spec = {1: (TType.MAP, 'emitted', (TType.STRING, (TType.MAP,
                                                             (TType.STRING,
                                                              TType.I64)))),
                   2: (TType.MAP, 'transferred', (TType.STRING,
                                                  (TType.MAP, (TType.STRING,
                                                               TType.I64)))),
                   3: (TType.STRUCT, 'specific', ExecutorSpecificStats)}


class ExecutorInfo(TPayload):
    thrift_spec = {1: (TType.I32, 'task_start'),
                   2: (TType.I32, 'task_end')}


class ExecutorSummary(TPayload):
    thrift_spec = {1: (TType.STRUCT, 'executor_info', ExecutorInfo),
                   2: (TType.STRING, 'component_id'),
                   3: (TType.STRING, 'host'),
                   4: (TType.I32, 'port'),
                   5: (TType.I32, 'uptime_secs'),
                   7: (TType.STRUCT, 'stats', ExecutorStats)}


class TopologyInfo(TPayload):
    thrift_spec = {1: (TType.STRING, 'id'),
                   2: (TType.STRING, 'name'),
                   3: (TType.I32, 'uptime_secs'),
                   4: (TType.LIST, 'executors', (TType.STRUCT,
                                                 ExecutorSummary)),
                   5: (TType.STRING, 'status'),
                   6: (TType.MAP, 'errors', (TType.STRING, (TType.LIST,
                                                            (TType.STRUCT,
                                                             ErrorInfo))))}


class KillOptions(TPayload):
    thrift_spec = {1: (TType.I32, 'wait_secs')}


class RebalanceOptions(TPayload):
    thrift_spec = {1: (TType.I32, 'wait_secs'),
                   2: (TType.I32, 'num_workers'),
                   3: (TType.MAP, 'num_executors', (TType.STRING, TType.I32))}


class TopologyInitialStatus(object):
    ACTIVE = 1
    INACTIVE = 2


class SubmitOptions(TPayload):
    thrift_spec = {1: (TType.I32, 'initial_status')}


##### NIMBUS SERVICE


class DRPCRequest(TPayload):
    thrift_spec = {1: (TType.STRING, 'func_args'),
                   2: (TType.STRING, 'request_id')}


class DRPCExecutionException(TException):
    thrift_spec = {1: (TType.STRING, 'msg')}



#### DistributedRPC service


#### DistributedRPCInvocations service
